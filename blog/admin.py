from django.contrib import admin
from .models import Author, Article, Label, Comment

# Register your models here.
admin.site.register(Author)
admin.site.register(Article)
admin.site.register(Label)
