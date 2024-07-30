from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('create_post/', create_post, name='create_post'),
    path('create_category/', create_category, name='create_category'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('edit_category/<int:pk>/', edit_category, name='edit_category'),
    path('delete_category/<int:pk>/', delete_category, name='delete_category'),
    path('edit_post/<int:pk>/', edit_post, name='edit_post'),
    path('delete_post/<int:pk>/', delete_post, name='delete_post'),
    path('add_comment/<int:pk>/', add_comment, name='add_comment'),
    path('category_fillter/', category_filter, name='category_filter'),
    path('author_fillter/', author_filter, name='author_filter'),
]