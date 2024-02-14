from django.db import models

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
    
class Comment:
    # author_name        اختیاری
    # email              اختیاری
    # text               اجباری
    # datetime_created   
    # post                اجباری و مربوط به یک پست خاص
    pass
    