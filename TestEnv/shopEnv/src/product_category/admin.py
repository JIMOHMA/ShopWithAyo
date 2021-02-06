from django.contrib import admin

# Import a single model
from .models import Product

# import all model(s)
# from .models import *

# Register your models here.
admin.site.register(Product)