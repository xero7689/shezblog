from django.shortcuts import render
from .models import Article, Author

# Create your views here.


def blog(request):
    author = Author.objects.get(name='shz')
    archives = author.article_set.dates('create_date', 'month', order='DESC')
    context = {'author': author, 'archives': archives}
    return render(request, 'blog.html', context)
