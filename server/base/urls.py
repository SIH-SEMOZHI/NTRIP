from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('getLoc', views.satellite, name='getLoc')

]
