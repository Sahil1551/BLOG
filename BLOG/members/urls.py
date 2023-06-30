from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('education/',views.education,name='education'),
    path('awards/', views.awards, name='awards'),
    path('interest/', views.interest, name='interest'),
    path('projects/', views.projects, name='projects'),
]