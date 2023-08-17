#I create to put db entities in superuser page

from django.contrib import admin
from .models import Drink

admin.site.register(Drink)