from django.shortcuts import render, get_object_or_404
from .models import Post
import markdown


# Create your views here.
def index(request, page):
    post_list = Post.objects.order_by('-created_time')[(page - 1) * 5:page * 5]
    return render(request, 'blog/index.html', {
        'post_list': post_list,
    })


def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.body = markdown.markdown(post.body, extensions=['markdown.extensions.toc', 'markdown.extensions.sane_lists',
                                                         'markdown.extensions.codehilite',
                                                         'markdown.extensions.fenced_code'])
    comment_list = Comment.objects.filter(post=post_id).order_by('-created_time')
    return render(request, 'blog/detail.html', {'post': post, 'comment_list': comment_list})


def archives(request, year, month):
    post_list = Post.objects.filter(created_time__year=year, created_time__month=month)
    return render(request, 'blog/index.html', {'post_list': post_list})


def categories(request, category):
    post_list = Post.objects.filter(id=category)
    return render(request, 'blog/index.html', {'post_list': post_list})
#
#
# def about(request):
#     return render(request, 'blog/about.html')
#
#
# def contact(request):
#     return render(request, 'blog/contact.html')
