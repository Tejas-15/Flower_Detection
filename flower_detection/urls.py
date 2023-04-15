from django.urls import path
from . import views
from .views import upload

urlpatterns = [
    path('', views.home , name='main_home'),
    path('home/', views.home , name='upload'),
    path('daisy/', views.daisy , name='daisy'),
    path('sunflower/', views.sunflower , name='sunflower'),
    path('rose/', views.rose , name='rose'),
    path('tulip/', views.tulip , name='tulip'),
    path('dandelion/', views.dandelion , name='dandelion'),
    path('lotus/', views.lotus , name='lotus'),
    path('Test1/', views.Test1 , name='Test1'),
    path('About/', views.About , name='About'),
    path('Help/', views.Help , name='Help'),
]
