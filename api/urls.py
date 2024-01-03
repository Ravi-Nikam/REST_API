from django.contrib import admin
from django.urls import path
from . import views
import views

urlpatterns = [
    path('index/',views.index,name='index'),
    # path('api/Account',AccountInformation.as_view()),
    # path('api/Account/<int:pk>',AccountDetails.as_view()),
]