from django.contrib import admin
from django.urls import path,include
from api.views import AccountInformation,AccountDetails

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/Account',AccountInformation.as_view()),
    path('api/Account/<int:pk>',AccountDetails.as_view()),
    # path('',include('api.urls')),
]
