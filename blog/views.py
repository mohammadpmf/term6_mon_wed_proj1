from django.shortcuts import render


def show_all_posts(request):
    return render(request, 'posts_list.html')

def new_post(request):
    return render(request, 'new_post.html')

def detail(request, pk):
    return render(request, 'post_detail.html')
