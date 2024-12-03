from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create_blog/', views.create_blog, name='create_blog'),
    path('view_blog/<int:blog_id>/', views.view_blog, name='view_blog'),
    path('my_blogs/', views.my_blogs, name='my_blogs'),
    path('view_my_blogs/<int:blog_id>/', views.view_my_blog, name='view_my_blog'),
    path('delete_blog/<int:blog_id>/', views.delete_blog, name='delete_blog'),
    path('update_blog/<int:blog_id>/', views.update_blog, name='update_blog'),
    path('update/<int:blog_id>/', views.update, name='update'),
]
