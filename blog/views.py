from django.shortcuts import render
from .models import Article, Label

# Create your views here.
def blog(request):
    return render(request, 'blog.html')
