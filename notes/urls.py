import profile

from django.urls import path
from . import views


urlpatterns = [




    path('upload_notes/', views.upload_notes, name='upload_notes'),
    path('view_mynotes/', views.view_mynotes, name='view_mynotes'),
    path('delete_mynotes/<int:pid>/', views.delete_mynotes, name='delete_mynotes'),

    path('viewallnotes/', views.viewallnotes, name='viewallnotes'),

]
