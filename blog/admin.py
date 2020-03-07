from django.contrib import admin
from .models import Article, About, Label, Comment

# Register your models here.
admin.site.register(About)
admin.site.register(Article)
admin.site.register(Label)
