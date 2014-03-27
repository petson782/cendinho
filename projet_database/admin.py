from django.contrib import admin
from models import Cours,Programme,Professeurs,DescriptionCours

# Register your models here.

class profadmin(admin.ModelAdmin):
    list_display=('NomProf','PrenomProf','Email')
    search_fields=('NomProf','PrenomProf')


admin.site.register(Cours)
admin.site.register(Programme)
admin.site.register(Professeurs,profadmin)
admin.site.register(DescriptionCours)
