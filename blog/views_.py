from django.shortcuts import render, redirect, get_object_or_404
from .models import BlogPost, Comment
from .forms import BlogPostForm

def tag(request):
    if request.method=='POST':
        tag=request.POST.get('tag')
        posts = BlogPost.objects.filter(tag=tag).order_by("-datetime_modified")
        context = {
            "posts" : posts
        }
        return render(request, 'posts_list.html', context)
    return render(request, 'search.html')
    


def show_all_posts(request):
    posts = BlogPost.objects.filter(status="p").order_by("-datetime_modified")
    context = {
        "posts" : posts
    }
    return render(request, 'posts_list.html', context)

def new_post(request):
    form = BlogPostForm()
    if request.method=='POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'new_post.html', {'form': form})


def update(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    form = BlogPostForm(instance=post)
    if request.method=='POST':
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'update_post.html', {'form': form})

def detail(request, pk):
    # post = BlogPost.objects.get(pk=pk)
    post = get_object_or_404(BlogPost, pk=pk)
    comments = Comment.objects.filter(post=post).order_by('-datetime_created')
    context = {
        'post': post,
        'comments': comments,
    }
    if request.method=='POST':
        author_name = request.POST.get('author_name')
        email = request.POST.get('email')
        text = request.POST.get('text')
        Comment.objects.create(
            author_name=author_name,
            email=email,
            text=text,
            post=post,
        )
    return render(request, 'post_detail.html', context)

def delete(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    context = {
        'post': post
    }
    if request.method=='POST':
        post.delete()
        return redirect('home')
    return render(request, 'delete_post.html', context)
