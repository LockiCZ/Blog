from django.conf import settings
from django.db import models
from django.utils import timezone
from django.urls import reverse

from martor.models import MartorField


class Post(models.Model):
    author = models.ForeignKey('users.User', on_delete=models.RESTRICT, related_name="post_author")

    title = models.CharField(max_length=200)
    url_name = models.CharField(max_length=50, db_index=True)
    version = models.CharField(max_length=20)
    lang = models.CharField(max_length=2, db_index=True, choices=settings.LANGUAGES)

    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True, null=True)
    thumbnail_caption = MartorField()

    content = MartorField()

    last_update_by = models.ForeignKey('users.User', on_delete=models.RESTRICT, related_name="post_update_by")
    last_update_date = models.DateTimeField(default=timezone.now)

    created_date = models.DateTimeField(default=timezone.now)
    publish_date = models.DateTimeField(blank=True, null=True, db_index=True)

    published = models.BooleanField(default=False)

    def approve_comments(self):
        return self.comments.filter(approved_comment=True)

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={'pk': self.pk})

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        'blog.Post', related_name='comments', on_delete=models.RESTRICT)
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse("post_list")

    def __str__(self):
        return self.text


class Quote(models.Model):
    author = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    company = models.CharField(max_length=200)
    quote = models.CharField(max_length=3000)

    def __str__(self):
        return self.quote
