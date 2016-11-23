#coding: utf-8

import os
import io
from django.core.management.base import BaseCommand
from core.models import Category
from django.template.loader import render_to_string
from django.conf import settings

class Command(BaseCommand):
    help = 'builds a category tree'

    def handle(self, *args, **options):
        template_path = os.path.join(settings.BASE_DIR, "templates", "category_tree.html")
        rendered_path = os.path.join(settings.BASE_DIR, "templates", "cached", "category_tree_rendered.html")
        io.open(rendered_path, 'w', encoding='utf8').write(render_to_string(template_path, {'categories': Category.objects.filter(pid__isnull=True)}))
            
