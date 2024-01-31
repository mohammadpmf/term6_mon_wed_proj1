from django.shortcuts import render
from .models import BlogPost


def show_all_posts(request):
    posts = BlogPost.objects.filter(status="p").order_by("-datetime_modified")
    context = {
        "posts" : posts
    }
    return render(request, 'posts_list.html', context)

def new_post(request):
    return render(request, 'new_post.html')

def detail(request, pk):
    return render(request, 'post_detail.html')