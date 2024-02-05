from django.shortcuts import render, get_object_or_404
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
    # post = BlogPost.objects.get(pk=pk)
    post = get_object_or_404(BlogPost, pk=pk)
    context = {
        'post': post
    }
    return render(request, 'post_detail.html', context)
