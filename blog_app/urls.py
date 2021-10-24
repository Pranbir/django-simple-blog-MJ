from django.urls import path
from . import views

app_name = 'blog_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('search', views.search, name='search'),
    path('post/<id>', views.single_post, name='single_post'),
]
