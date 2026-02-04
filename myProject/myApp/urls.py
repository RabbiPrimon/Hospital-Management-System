from django.contrib import admin
from django.urls import path
from myApp.views import *


urlpatterns = [
    path('',homePage,name="homePage"),
    path('doctorPage/',doctorPage,name="doctorPage"),
    path('patientPage/',patientPage,name="patientPage"),
    path('appointmentPage/',appointmentPage,name="appointmentPage"),
    path('departmentPage/',departmentPage,name="departmentPage"),
    path('loginPage/',loginPage,name="loginPage"),
    path('signupPage/',signupPage,name="signupPage"),
    path('logoutPage/',logoutPage,name="logoutPage"),
    
    
    path('DoctordeletePage/<int:id>',DoctordeletePage,name="DoctordeletePage"),
    path('DoctoreditPage/<int:id>',DoctoreditPage,name="DoctoreditPage"),
    
    
]