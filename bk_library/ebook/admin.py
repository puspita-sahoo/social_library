from django.contrib import admin
from .models import EBooksModel



@admin.register(EBooksModel)
class EBooksadmin(admin.ModelAdmin):
    pass
#     list_display = ('titlee', 'pdf')














