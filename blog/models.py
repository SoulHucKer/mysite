from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)

    def get_absolute_url(self):
        return "blog/category/%i/" % self.id

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=20)

    def get_absolute_url(self):
        return "blog/tag/%i/" % self.id

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=70)
    body = models.TextField()
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    excerpt = models.CharField(max_length=200, blank=True)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField(Tag)

    def get_absolute_url(self):
        return "/blog/post/%i/" % self.id

    def __str__(self):
        return self.title
