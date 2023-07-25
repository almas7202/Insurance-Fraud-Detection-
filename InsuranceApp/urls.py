
from django.urls import path,include
from . import views
from InsuranceApp.views import *

urlpatterns = [
    path('base/',views.baseview,name='baseview')
    
]