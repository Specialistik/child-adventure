from django.shortcuts import render
from models import Category, Product, Article


def index(request):
    return render(request, 'index.html', {'categories': Category.objects.filter(pid__isnull=True), 'articles': Article.objects.all()})
    

def category(request, id, url):
    if Category.objects.get(pk=id).has_children():
        return category_list(request, id, url)
    else:
        return category_items(request, id, url)


def category_list(request, id, url):
    return render(request, 'category_list.html', {'categories': Category.objects.filter(category=id)})
    
    
def category_items(request, id, url):
    return render(request, 'category_items.html', {'categories': Product.objects.filter(category=id)})


def article(request, id, url):
    return render(request, 'article.html', {'categories': Category.objects.filter(pid__isnull=True), 'article': Article.objects.get(pk=id)})


def product(request, id, url):
    return render(request, 'product.html')
