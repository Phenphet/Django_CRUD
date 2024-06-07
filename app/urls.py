from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('create/', views.createHome, name="home_create"),
    path('student/<int:id>/edit/', views.editHome, name="home_edit"),
    path('student/<int:id>/detail/', views.detailHome, name="home_detail"),
    path('student/<int:id>/delete/', views.deleteHome, name="home_delete"),
]