from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('record/',views.record),
    path('dgnss/',views.process),

]