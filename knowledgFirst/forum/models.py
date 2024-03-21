from django.db import models
from django.urls import reverse

CATEGORY_CHOICES = [
    ('Sport', 'Sport'),
    ('Nature', 'Nature'),
    ('IT', 'IT'),
    ('Food', 'Food'),
    ('Fashion', 'Fashion')
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
    ('Moderator/Administrator', 'Moderator/Administrator'),
]

# Accessing the first element of the GRADES_CHOICES list of tuples
DEFAULT_GRADE = GRADES_CHOICES[0][0]  # 'Novice'

class Grade(models.Model):
    name = models.CharField(max_length=20, choices=GRADES_CHOICES, default=DEFAULT_GRADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('grade-detail', kwargs={'pk': self.pk})


class User(models.Model):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    join_date = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    grade = models.ForeignKey(Grade, on_delete=models.SET_NULL, null=True, default=None)
    total_posts = models.IntegerField(default=0)
    total_comments = models.IntegerField(default=0)
    total_likes = models.IntegerField(default=0)
    interests = models.TextField()
    followers = models.IntegerField(default=0)
    following = models.IntegerField(default=0)

    def __str__(self):
        return self.username


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    last_modify = models.DateTimeField(auto_now=True)
    total_replies = models.IntegerField(default=0)
    state = models.CharField(max_length=20, choices=POST_STATE_CHOICES, default='Open')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, blank=True, null=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pinned = models.BooleanField(default=False)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.author.username} - {self.post.title}"


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


class PostLike(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.post.title} - {self.user.username}"


class CommentLike(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.comment.author.username} - {self.user.username}"

    def get_absolute_url(self):
        return reverse('user-detail', kwargs={'pk': self.pk})


class UserFollow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower')
    followee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followee')

    def __str__(self):
        return f"{self.follower.username} - {self.followee.username}"

    def get_absolute_url(self):
        return reverse('user-detail', kwargs={'pk': self.follower.pk})
