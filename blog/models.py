from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


STATUS = [
    ('published', 'Published'),
    ('draft', 'Draft'),
]


class Category(models.Model):
    name = models.CharField(max_length=100, default='django')

    def __str__(self):
        return self.name
    

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    create_post = models.DateTimeField(default=datetime.now())
    body = models.TextField()
    likes = models.ManyToManyField(User, related_name="post_likes", null=True, blank=True)
    status = models.CharField(choices=STATUS, max_length=10, default='Draft')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    
    def total_likes(self):
        return self.likes.count()
    
    def __str__(self):
        return '{} - {}'.format(self.title, self.author )


class Comment(models.Model):
    user_cooment = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    mycomment = models.TextField()
    date_add = models.DateTimeField(default=datetime.now())
    
    def __str__(self):
        return '{} - {}'.format(self.post.title, self.user_cooment.username)
    




