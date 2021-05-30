from django.urls import path

from . import views

app_name = 'crews'
urlpatterns = [
    path("", views.team_list, name='index'),
    path('<int:pk>/', views.team_detail, name='team_detail'),
    path('new', views.team_new, name='team_new'),
    path('success/', views.team_list, name='index'),
    path('newmember', views.member_new, name='member_new'),
    path('delete', views.member_delete, name='member_delete'),
]