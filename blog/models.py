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
    # author = models.ForeignKey()
    