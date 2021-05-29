from django.urls import path

from . import views

app_name = 'crews'
urlpatterns = [
    path("", views.team_list, name='index'),
    #path('', views.IndexView.as_view(), name='index'),
    #path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/', views.team_detail, name='team_detail'),
    path('new', views.team_new, name='team_new'),
    path('success/', views.team_list, name='index'),
]