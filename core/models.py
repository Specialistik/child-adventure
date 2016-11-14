#coding: utf-8

from __future__ import unicode_literals
from django.db import models
from ckeditor.fields import RichTextField

class Substance(models.Model):
    title = models.CharField(max_length=80, null=True, blank=True, verbose_name=u'Заголовок')
    keywords = models.CharField(max_length=20, null=True, blank=True, verbose_name=u'Ключевые слова')
    description = models.CharField(max_length=200, null=True, blank=True, verbose_name=u'Описание')
    url = models.CharField(max_length=80, null=True, blank=True, verbose_name=u'Человеко-понятный URL')
    
    def get_pic(self, width=350, height=200):
        return self.pic if self.pic else '/static/images/no_pic.jpg'

    def __repr__(self):
        return self.title if self.title is not None else u'empty'
    
    def __str__(self):
        return self.title if self.title is not None else u'empty'
    
    def __unicode__(self):
        return self.title if self.title is not None else u'empty'
    
    class Meta:
        abstract = True


class Category(Substance):
    pid = models.ForeignKey("self", null=True, blank=True, verbose_name=u"Родительская категория")
    pic = models.ImageField(upload_to='media/category', null=True, blank=True)

    def children(self):
        return Category.objects.filter(pid=self.id)

    def has_children(self):
        if len(Category.objects.filter(pid=self.id)) > 0:
            return True
        return False

    class Meta:
        db_table = 'categories'
        verbose_name = u'Категория'
        verbose_name_plural = u'Категории'
    

class Product(Substance):
    category = models.ForeignKey(Category, verbose_name=u"Категория")
    pic = models.ImageField(upload_to='media/product', null=True, blank=True)
    
    class Meta:
        db_table = 'products'
        verbose_name = u'Товар'
        verbose_name_plural = u'Товары'
    

class Article(Substance):
    text = RichTextField()
    pic = models.ImageField(upload_to='media/article', null=True, blank=True)
    
    class Meta:
        db_table = 'articles'
        verbose_name = u'Статья'
        verbose_name_plural = u'Статьи'
