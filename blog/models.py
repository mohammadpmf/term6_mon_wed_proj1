from django.db import models
from django.urls import reverse

class BlogPost(models.Model):
    STATUS_CHOICES = (
        ('p', 'published'),
        ('d', 'draft'),
    )
    title = models.CharField(max_length=100)
    text = models.TextField()
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    tag = models.CharField(max_length=100, default='original')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk": self.pk})
        
    
class Comment(models.Model):
    author_name =models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    text = models.TextField()
    datetime_created = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(to=BlogPost, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.text
    