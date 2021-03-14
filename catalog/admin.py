from django.contrib import admin
from .models import Tovar, Rubric
# Register your models here.

class TovarAdmin(admin.ModelAdmin):
    list_display = ('name', 'cena', 'rubric')
    list_display_links = ('name', 'cena', 'rubric')
    search_fields = ('name', 'cena')

#from .models import Rubric    

admin.site.register(Tovar, TovarAdmin)    

admin.site.register(Rubric)    
