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

DEFAULT_GRADE = GRADES_CHOICES[0][0]  # 'Novice'
DEFAULT_STATE = POST_STATE_CHOICES[0][0]  # 'Open'

class Grade(models.Model):
    name = models.CharField(max_length=30, choices=GRADES_CHOICES, default=None)

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
    grade = models.CharField(max_length=30, default=DEFAULT_GRADE)
    total_posts = models.IntegerField(default=0)
    total_replys = models.IntegerField(default=0)
    total_likes = models.IntegerField(default=0)
    interests = models.TextField()
    followers = models.IntegerField(default=0)
    following = models.IntegerField(default=0)

    def __str__(self):
        return self.username


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    last_modify = models.DateTimeField(auto_now=True)
    total_replies = models.IntegerField(default=0)
    state = models.CharField(max_length=20, choices=POST_STATE_CHOICES, default=DEFAULT_STATE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, blank=True, null=True)

    def delete(self, *args, **kwargs):
        self.update_posts()
        super(User, self).delete(*args, **kwargs)

    def update_posts(self):
        deleted_user = User.objects.get_or_create(username='deleted')[0]
        self.post_set.update(author=deleted_user)
    
    def __str__(self):
        return self.title


class Reply(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    reply_date = models.DateTimeField(auto_now_add=True)
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


class ReplyLike(models.Model):
    reply = models.ForeignKey(Reply, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.reply.author.username} - {self.user.username}"

    def get_absolute_url(self):
        return reverse('user-detail', kwargs={'pk': self.pk})


class UserFollow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower')
    followee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followee')

    def __str__(self):
        return f"{self.follower.username} - {self.followee.username}"

    def get_absolute_url(self):
        return reverse('user-detail', kwargs={'pk': self.follower.pk})
