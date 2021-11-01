from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserListView.as_view()),
    path('files/', views.FileListView.as_view()),
    path('push/', views.PushListView.as_view()),
    path('sms/', views.SmsListView.as_view()),
    path('spnavigator/', views.SpnListView.as_view()),
    path('lk/', views.LkListView.as_view()),
]