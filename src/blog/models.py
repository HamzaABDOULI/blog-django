from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    post_date = models.DateTimeField(default = timezone.now)
    post_apdate = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta :
        ordering = ('-post_date',)   


class Comment(models.Model):
    name = models.CharField(max_length=100) 
    email = models.EmailField()
    body = models.TextField()
    comment_date = models.DecimalField(auto_now_add = True)
    active = models.BooleanField(default=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')        


