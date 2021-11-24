from django.urls import path

from . import views

urlpatterns = [
    path('test_form/', views.TestView, name="TestForm"),
    path('', views.index, name="index"),
]
