from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_all_posts, name='home'),
    path('new_post/', views.new_post, name='new_post'),
    path('detail/<int:pk>/', views.detail, name='detail'),
]
