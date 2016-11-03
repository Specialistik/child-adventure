from django.core.management.base import BaseCommand
from core.models import Product, Category
from transliterate import translit

class Command(BaseCommand):
    help = 'makes translite for human friendly URLs'

    def handle(self, *args, **options):
        for category in Category.objects.all():
            category_url = translit(category.title, 'ru', reversed=True) 
            category.url = category_url.replace(' ', '_')[0:150]
            category.save()

        for product in Product.objects.exclude(url__isnull=True).exclude(url__exact=''):
            product_url = translit(product.title, 'ru', reversed=True) 
            product.url = product_url.replace(' ', '_')[0:150]
            product.save()

            
