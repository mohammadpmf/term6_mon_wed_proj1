from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from .models import BlogPost, Comment
from .forms import BlogPostForm, CommentForm
from django.views import generic

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

class AllPosts(generic.ListView):
    model = BlogPost
    template_name = 'posts_list.html'
    context_object_name = 'posts'

    # def get_queryset(self):
    #     return BlogPost.objects.filter(status="p").order_by("-datetime_modified")
    
def new_post(request):
    form = BlogPostForm()
    if request.method=='POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'new_post.html', {'form': form})

class NewPost(generic.CreateView):
    model = BlogPost
    template_name = 'new_post.html'
    form_class = BlogPostForm
    success_url = reverse_lazy('home')
    # fields = ['title', 'text', 'status', 'author']


def update(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    form = BlogPostForm(instance=post)
    if request.method=='POST':
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'update_post.html', {'form': form})

class Update(generic.UpdateView):
    model = BlogPost
    template_name = 'update_post.html'
    form_class = BlogPostForm


def detail(request, pk):
    # post = BlogPost.objects.get(pk=pk)
    post = get_object_or_404(BlogPost, pk=pk)
    comments = Comment.objects.filter(post=post, status=True).order_by('-datetime_created')
    form = CommentForm()
    if request.method=='POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post=post
            new_comment.save()
            form = CommentForm()

    context = {
        'post': post,
        'comments': comments,
        'form': form,
    }
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
