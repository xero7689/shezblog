from django.db import models

class Label(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    create_date = models.DateTimeField()

class Article(models.Model):
    title = models.CharField(max_length=64)
    abstract = models.TextField()
    content = models.TextField()
    lables = models.ManyToManyField(Label)
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField()

class Comment(models.Model):
    author = models.CharField(max_length=64)
    content = models.TextField()
    create_date = models.DateTimeField()
