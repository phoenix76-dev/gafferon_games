from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import *


def index(request):
    try:
        articles = Article.objects.all()[:15]
    except IndexError:
        articles = Article.objects.all()
    ctx = {'title_block_name': 'fragments/index_header_block.html',
           'articles': articles}
    return render(request, 'list.html', ctx)


def by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    articles = Article.objects.filter(category=category)
    ctx = {'title_block_name': 'fragments/category_header_block.html',
           'category_name': category.title,
           'articles': articles}
    return render(request, 'list.html', ctx)


def by_tag(request, tag_id):
    tag = get_object_or_404(Tag, id=tag_id)
    articles = tag.articles.all()
    ctx = {'title_block_name': 'fragments/tag_header_block.html',
           'tag_name': tag.title,
           'articles': articles}
    return render(request, 'list.html', ctx)


def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    ctx = {'title_block_name': 'fragments/article_detail_header_block.html',
           'article': article}
    return render(request, 'article_detail.html', ctx)


def about(request):
    ctx = {'title': 'About',
           'user': User.objects.get(username='glenn_f')}
    return render(request, 'about.html', ctx)
