from django.contrib import admin
from .models import Author, Article, Label, Comment

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'add_date')

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'create_date', 'modify_date', 'author', 'visible')

class LabelAdmin(admin.ModelAdmin):
    list_display = ('name', 'create_date')

# Register your models here.
admin.site.register(Author, AuthorAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Label, LabelAdmin)
