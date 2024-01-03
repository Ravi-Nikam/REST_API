from django.shortcuts import render
from rest_framework import generics
from .models import Account
from .seriazlizers import AccountSerializer


class AccountInformation(generics.ListCreateAPIView):
    queryset=Account.objects.all()
    serializer_class=AccountSerializer


class AccountDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset=Account
    serializer_class=AccountSerializer


# Create your views here.
def index(request):
    return render(request, './index.html')