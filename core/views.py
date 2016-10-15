from django.shortcuts import render
from models import Category, Product, Article


def index(request):
    return render(request, 'index.html', {'categories': Category.objects.filter(pid__isnull=True), 'articles': Article.objects.all()})
    

def category_list(request, id):
    return render(request, 'category_list.html', {'categories': Category.objects.filter(category=id)})
    
    
def category_items(request, id):
    return render(request, 'category_items.html', {'categories': Product.objects.filter(category=id)})