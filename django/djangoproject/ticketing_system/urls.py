from django.urls import path

from . import views

urlpatterns = [
    path('test_form/', views.TestView, name="TestForm"),
    path('success/', views.successView, name="SuccessView"),
    path('', views.indexView, name="indexView"),
]
