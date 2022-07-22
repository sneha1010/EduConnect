from django.urls import path,include

from base import views

urlpatterns = [

    path('chatRoom/', views.home, name="home"),
    path('room/<str:pk>/', views.room, name="room"),
    path('create-room/', views.createRoom, name="create-room"),
    path('update-room/<str:pk>/', views.updateRoom, name="update-room"),
    path('delete-room/<str:pk>/', views.deleteRoom, name="delete-room"),
    path('delete-message/<str:pk>/', views.deleteMessage, name="delete-message"),
    path('topics/', views.topicsPage, name="topics"),
    path('profile/<str:pk>/', views.userProfile, name="user-profile"),
    path('activity/', views.activityPage, name="activity"),
    path('update-user/', views.updateUser, name="update-user"),
    # patterns('', url(r'^chatRoom/', include('chatRoom.urls')))
]
