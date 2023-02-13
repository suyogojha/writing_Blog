from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('article/<str:slug>', views.detail, name = 'detail'),
    path('create-post', views.createPost, name = 'create'),
    path('article/update/<str:slug>', views.editPost, name = 'edit'),
    path('article/delete/<str:slug>', views.deletePost, name = 'delete'),
    path('category/<str:slug>', views.tagPage, name = 'tag'),
]