#coding: utf-8

from __future__ import unicode_literals
from django.db import models


class Substance(models.Model):
    title = models.CharField(max_length=80, null=True, verbose_name=u'Заголовок')
    keywords = models.CharField(max_length=20, null=True, verbose_name=u'Ключевые слова')
    description = models.CharField(max_length=200, null=True, verbose_name=u'Описание')
    url = models.CharField(max_length=80, null=True, verbose_name=u'Человеко-понятный URL')
    
    def __repr__(self):
        return self.title
    
    def __str__(self):
        return self.title
    
    #def __unicode__(self):
    #    return self.title
    
    class Meta:
        abstract = True


"""
class Image(models.Model):
    path = models.CharField(max_length=256, null=True, verbose_name=u"Относительный путь до изображения")
    #pic = models.ImageField(null=True, blank=True, verbose_name=u"Изображение")
    
    class Meta:
        db_table = 'images'
        verbose_name = u'Изображение'
        verbose_name_plural = u'Изображения'
"""


class Category(Substance):
    pid = models.ForeignKey("self", null=True, blank=True, verbose_name=u"Родительская категория")
    #pic = models.ForeignKey(Image, null=True, blank=True, verbose_name=u"Изображение")

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
    #pic = models.ForeignKey(Image, null=True, blank=True, verbose_name=u"Изображение")
    
    class Meta:
        db_table = 'products'
        verbose_name = u'Товар'
        verbose_name_plural = u'Товары'
    

class Article(models.Model):
    text = models.TextField(blank=True, verbose_name=u"Текст статьи")
    #pic = models.ForeignKey(Image, null=True, blank=True, verbose_name=u"Изображение")
    
    class Meta:
        db_table = 'articles'
        verbose_name = u'Статья'
        verbose_name_plural = u'Статьи'