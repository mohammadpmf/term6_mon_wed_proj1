from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_all_posts, name='home'),
    path('new_post/', views.new_post, name='new_post'),
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('update/<int:pk>/', views.update, name='update'),
    path('tag/', views.tag, name='tag'),
]
