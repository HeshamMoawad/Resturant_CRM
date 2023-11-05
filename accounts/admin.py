from django.contrib import admin 
from .models import (
    Account ,
    Address,
    Area ,
    City ,


    models ,
)

class CityAdmin(admin.ModelAdmin):
    list_display = ["name","creator","created_at"]

admin.site.register(City , CityAdmin)


admin.site.register(Area)
admin.site.register(Address)
admin.site.register(Account)
