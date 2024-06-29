from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse
from jakubKrol_zaliczenie.models import Article

def indexArticleJson(request):
    articles = Article.objects.all()
    data = serializers.serialize('json', articles)
    return HttpResponse(data, content_type='application/json')

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the the best app ;)")

def indexArticle(request):
    title = 'Lista artykułów'
    articles = Article.objects.all()
    return render(request, 'articles.html', {
        "articles": articles,
        "title": title,
    })