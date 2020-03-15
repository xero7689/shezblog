from django.db import models
from django.utils.timezone import now
from ckeditor.fields import RichTextField


class Author(models.Model):
    name = models.CharField(max_length=64)
    about = RichTextField()
    add_date = models.DateTimeField(default=now)


class Article(models.Model):
    title = models.CharField(max_length=64)
    abstract = models.CharField(max_length=128)
    content = RichTextField()
    create_date = models.DateTimeField(default=now)
    modify_date = models.DateTimeField(default=now)
    author = models.ForeignKey(Author, default=None, on_delete=models.CASCADE)
    visible = models.BooleanField(default=True)


class Label(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    create_date = models.DateTimeField(default=now)
    articles = models.ManyToManyField(Article)


class Comment(models.Model):
    author = models.CharField(max_length=64)
    content = models.TextField()
    create_date = models.DateTimeField()
    articles = models.ForeignKey(
        Article, default=None, on_delete=models.CASCADE)
