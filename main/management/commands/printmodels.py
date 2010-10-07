# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from django.db import models


class Command(BaseCommand):
    args = ''
    help = 'Print project models list with number of objects for each model'

    def handle(self, *args, **options):
        models_list = models.get_models()
        print("%s models found:" % len(models_list))
        for  model in models_list:
            print("%s: %s object(s)" % (model, model.objects.count()))
