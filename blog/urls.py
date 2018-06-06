from django.urls import path
from . import views
from django.views.generic.base import TemplateView

app_name = 'blog'
urlpatterns = [
    path('<int:page>/', views.index, name='index'),
    path('<int:year>/<int:month>/', views.archives, name='archives'),
    path('category/<int:category>/', views.categories, name='categories'),
    path('post/<int:post_id>/', views.detail, name='detail'),
    path('about/', TemplateView.as_view(template_name="blog/about.html"), name='about'),
    path('contact/', TemplateView.as_view(template_name="blog/contact.html"), name='contact'),
    path('full-width/', TemplateView.as_view(template_name="blog/full-width.html"), name='full-width'),
]
