from django.urls import  path
from . import views

urlpatterns = [
    path("student_home/",views.home,name="Home"),
    # path("chatbot/", views.chatbot, name="ChatBot"),
    path("notes/", views.Notes, name="Notes"),
    path("allnotes/", views.viewallnotes, name="ALLNotes"),
    path("result/",views.result,name="Result"),
    path("timeTable/",views.timetable,name="TimeTable"),
    path("logout/",views.logout_request,name="logout"),



    
    
]