from django import template
from ..models import Post, Category, Tag
from django.db.models import Count
import math
register = template.Library()


@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-created_time')[:num]


@register.simple_tag
def archives():
    return Post.objects.dates('created_time', 'month', order='DESC')


@register.simple_tag
def get_categories():
    return Category.objects.values('name').annotate(Count('post'))


@register.simple_tag
def get_tags():
    return Tag.objects.all()


@register.simple_tag
def get_count():
    s = int(math.ceil(Post.objects.count() / 5))
    g = (x+1 for x in range(s))
    return g
