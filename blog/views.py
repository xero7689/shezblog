from django.shortcuts import render
from .models import Article, Label

# Create your views here.
def blog(request):
    latest_articles = Article.objects.order_by('create_date')[:5]
    context = {'latest_articles': latest_articles}
    print(context)
    return render(request, 'blog.html', context)
