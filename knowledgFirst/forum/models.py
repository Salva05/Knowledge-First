from django.db import models
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    total_replies = models.IntegerField(default=0)
    state = models.CharField(max_length=100, default='Open')
    author = models.CharField(max_length=100)
    likes = models.IntegerField(default=0)
    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100)
    pinned = models.BooleanField(default=False)
    likes = models.IntegerField(default=0)
    def __str__(self):
        return self.author + ' - ' + self.post.title
    
class Tag(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('tag-detail', kwargs={'pk': self.pk})

class PostTag(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    def __str__(self):
        return self.post.title + ' - ' + self.tag.name
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.post.pk})

class PostLike(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.CharField(max_length=100)
    def __str__(self):
        return self.post.title + ' - ' + self.user

class CommentLike(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user = models.CharField(max_length=100)
    def __str__(self):
        return self.comment.author + ' - ' + self.user

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField()
    join_date = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    grade = models.CharField(default='Novice', max_length=100)
    total_posts = models.IntegerField(default=0)
    total_comments = models.IntegerField(default=0)
    total_likes = models.IntegerField(default=0)
    interests = models.TextField()
    def __str__(self):
        return self.username
    def get_absolute_url(self):
        return reverse('user-detail', kwargs={'pk': self.pk})
    
class UserFollow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower')
    followee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followee')
    def __str__(self):
        return self.follower.username + ' - ' + self.followee.username
    def get_absolute_url(self):
        return reverse('user-detail', kwargs={'pk': self.follower.pk})