from django.contrib import admin
from .models import Sector, Business, StoreInfo

# Register your models here.
admin.site.register(Sector)
admin.site.register(Business)
admin.site.register(StoreInfo)
