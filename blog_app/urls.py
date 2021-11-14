from django.urls import path
from . import views

app_name = 'blog_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('search', views.search, name='search'),
    path('post/<id>', views.single_post, name='single_post'),
    path('add_comment/<id>', views.add_comment, name='add_comment'),
    path('author/<id>', views.author_post, name='author_post'),
    path('login/', views.login_user, name='login_user'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_user, name='logout_user'),
    path('contact/', views.contact, name='contact'),
]
