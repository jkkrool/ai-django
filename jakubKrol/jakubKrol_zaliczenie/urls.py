from django.urls import path
from jakubKrol_zaliczenie.views import index, indexArticle, indexArticleJson
urlpatterns = [
    path('test/', index),
    path('html/', indexArticle),
    path('articles/', indexArticleJson)
]