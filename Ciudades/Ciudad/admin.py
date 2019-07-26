from django.contrib import admin
from .models import Region, Municipio

# Register your models here.

class RegionAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre',)
    list_filter = ('codigo', 'nombre',)
    search_fields = ('codigo', 'nombre',)

class MunicipioAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre',)
    list_filter = ('codigo', 'nombre',)
    search_fields = ('codigo', 'nombre',)

admin.site.register(Region, RegionAdmin)
admin.site.register(Municipio, MunicipioAdmin)