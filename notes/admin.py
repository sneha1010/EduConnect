from django.contrib import admin
from .models import *
# Register your models here.

def accept(notesadmin,request,queryset):
    queryset.update(status='accept')

def reject(notesadmin,request,queryset):
    queryset.update(status='reject')

class NotesAdmin(admin.ModelAdmin):

    list_filter = ['status']
    list_display = ['branch','subject','status']
    actions = [accept,reject]
admin.site.register(Notes,NotesAdmin)