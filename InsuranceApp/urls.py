
from django.urls import path,include
from . import views
from InsuranceApp.views import *

urlpatterns = [
    path('base/',views.baseview,name='baseview'),
    path('index/',views.indexview,name='indexview'),
    path('auth/',views.authview,name='authview')

    
]