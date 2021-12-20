from django.contrib import admin
from .models import Laptop1


class LaptopAdmin(admin.ModelAdmin):
    list_display = ['company', 'model_name', 'ram', 'rom', 'price', 'weight', 'Processor']


# Register your models here.
admin.site.register(Laptop1,LaptopAdmin)
