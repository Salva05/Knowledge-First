# Generated by Django 5.0.3 on 2024-03-30 21:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Novice', 'Novice'), ('Regular Contributor', 'Regular Contributor'), ('Active Participant', 'Active Participant'), ('Community Leader', 'Community Leader'), ('Superuser', 'Superuser'), ('Moderator', 'Moderator')], default=None, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('content', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('last_modify', models.DateTimeField(auto_now=True)),
                ('total_replies', models.IntegerField(default=0)),
                ('state', models.CharField(choices=[('Open', 'Open'), ('Closed', 'Closed')], default='Open', max_length=20)),
                ('total_likes', models.IntegerField(default=0)),
                ('category', models.CharField(blank=True, choices=[('Sport', 'Sport'), ('Nature', 'Nature'), ('Food', 'Food'), ('Fashion', 'Fashion'), ('Animals', 'Animals'), ('Technology', 'Technology'), ('Science', 'Science'), ('Culture', 'Culture'), ('Music', 'Music'), ('Entertainment', 'Entertainment'), ('History', 'History'), ('Fiction', 'Fiction'), ('Art', 'Art'), ('Other', 'Other')], max_length=20, null=True)),
                ('views', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(default='static/avatars/user.png', upload_to='static/avatars/')),
                ('last_login', models.DateTimeField(auto_now=True)),
                ('grade', models.CharField(default='Novice', max_length=30)),
                ('total_posts', models.IntegerField(default=0)),
                ('replies', models.IntegerField(default=0)),
                ('total_likes', models.IntegerField(default=0)),
                ('interests', models.TextField()),
                ('followers', models.IntegerField(default=0)),
                ('following', models.IntegerField(default=0)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PostLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='forum.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='liked_posts', to='forum.profile')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.profile'),
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('reply_date', models.DateTimeField(auto_now_add=True)),
                ('pinned', models.BooleanField(default=False)),
                ('likes', models.IntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.profile')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.post')),
                ('reply_to_reply', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='forum.reply')),
            ],
        ),
        migrations.CreateModel(
            name='ReplyLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reply', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.reply')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.profile')),
            ],
        ),
        migrations.CreateModel(
            name='PostTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.post')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.tag')),
            ],
        ),
        migrations.CreateModel(
            name='UserFollow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('followee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followee', to='forum.profile')),
                ('follower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follower', to='forum.profile')),
            ],
        ),
    ]
