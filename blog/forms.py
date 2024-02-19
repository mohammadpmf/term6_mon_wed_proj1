from django.forms import ModelForm
from .models import BlogPost, Comment


class BlogPostForm(ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'text', 'status', 'author']

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['author_name', 'email', 'text']

