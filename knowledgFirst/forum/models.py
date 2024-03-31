from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

CATEGORY_CHOICES = [
    ('Sport', 'Sport'),
    ('Nature', 'Nature'),
    ('Food', 'Food'),
    ('Fashion', 'Fashion'),
    ('Animals', 'Animals'),
    ('Technology', 'Technology'),
    ('Science', 'Science'),
    ('Culture', 'Culture'),
    ('Music', 'Music'),
    ('Entertainment', 'Entertainment'),
    ('History', 'History'),
    ('Fiction', 'Fiction'),
    ('Art', 'Art'),
    ('Other', 'Other')
]

POST_STATE_CHOICES = [
    ('Open', 'Open'),
    ('Closed', 'Closed'),
]

GRADES_CHOICES = [
    ('Novice', 'Novice'),
    ('Regular Contributor', 'Regular Contributor'),
    ('Active Participant', 'Active Participant'),
    ('Community Leader', 'Community Leader'),
    ('Superuser', 'Superuser'),
    ('Moderator', 'Moderator'),
]

DEFAULT_GRADE = GRADES_CHOICES[0][0]  # 'Novice'
DEFAULT_STATE = POST_STATE_CHOICES[0][0]  # 'Open'

class Grade(models.Model):
    name = models.CharField(max_length=30, choices=GRADES_CHOICES, default=None)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('grade-detail', kwargs={'pk': self.pk})

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='static/avatars/', default='static/avatars/user.png')
    last_login = models.DateTimeField(auto_now=True)
    grade = models.CharField(max_length=30, default=DEFAULT_GRADE)
    total_posts = models.IntegerField(default=0)
    replies = models.IntegerField(default=0)
    total_likes = models.IntegerField(default=0)
    interests = models.TextField()
    followers = models.IntegerField(default=0)
    following = models.IntegerField(default=0)
    email = models.EmailField(unique=True)
    def display_name(self):
        return self.user.username + '<br> - <br>' + self.grade
    
    def __str__(self):
        return self.user.username

class Post(models.Model):
    title = models.CharField(max_length=70)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    last_modify = models.DateTimeField(auto_now=True)
    total_replies = models.IntegerField(default=0)
    state = models.CharField(max_length=20, choices=POST_STATE_CHOICES, default=DEFAULT_STATE)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    total_likes = models.IntegerField(default=0)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, blank=True, null=True)
    views = models.IntegerField(default=0)

    def get_categories():
        return [category for category, other in CATEGORY_CHOICES]
    
    def __str__(self):
        return self.title


class Reply(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    reply_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    pinned = models.BooleanField(default=False)
    likes = models.IntegerField(default=0)
    reply_to_reply = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, default=None)

    def __str__(self):
        return f"{self.author.user.username} - {self.post.title}"

class PostLike(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='liked_posts')

    def __str__(self):
        return f"{self.user.user.username} likes {self.post.title}"
    
class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tag-detail', kwargs={'pk': self.pk})


class PostTag(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.post.title} - {self.tag.name}"

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.post.pk})

class ReplyLike(models.Model):
    reply = models.ForeignKey(Reply, on_delete=models.CASCADE, related_name='reply_like')
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.reply.author.user.username} - {self.user.user.username}"

    def get_absolute_url(self):
        return reverse('user-detail', kwargs={'pk': self.pk})


class UserFollow(models.Model):
    follower = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='follower')
    followee = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='followee')

    def __str__(self):
        return f"{self.follower.user.username} - {self.followee.user.username}"

    def get_absolute_url(self):
        return reverse('user-detail', kwargs={'pk': self.follower.pk})
