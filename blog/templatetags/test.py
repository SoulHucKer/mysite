from blog.models import Post
from django.db.models import Count, Sum

a = Post.objects.get(id=1)
