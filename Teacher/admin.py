from django.contrib import admin
from .models import *
# Register your models here.
class AnnouncementsAdmin(admin.ModelAdmin):
    list_display = ['text']

class ClassAdmin(admin.ModelAdmin):
    list_display = ['subject','date','time_start','time_end']

class ExamAdmin(admin.ModelAdmin):
    list_display = ['subject','date','time_start','time_end']

admin.site.register(Announcements,AnnouncementsAdmin)
admin.site.register(Class,ClassAdmin)
admin.site.register(Exam,ExamAdmin)