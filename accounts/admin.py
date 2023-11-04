from django.contrib import admin
from .models import (
    Account ,
    Address,
    Area ,
    City ,
)


# Register your models here.
admin.site.register(City)
admin.site.register(Area)
admin.site.register(Address)
admin.site.register(Account)
