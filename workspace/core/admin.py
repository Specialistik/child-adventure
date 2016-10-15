#coding: utf-8

from django.contrib import admin
from core.models import Article, Category, Product


class ArticleAdmin(admin.ModelAdmin):
    fields = ('title', 'keywords', 'description', 'url', 'text')
    list_display = ('title', 'url')
    
    
class CategoryAdmin(admin.ModelAdmin):
    fields = ('title', 'keywords', 'description', 'url', 'pid')
    list_display = ('title', 'url')
    
    
class ProductAdmin(admin.ModelAdmin):
    fields = ('title', 'keywords', 'description', 'url', 'pid')
    list_display = ('title', 'url')


admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Product)