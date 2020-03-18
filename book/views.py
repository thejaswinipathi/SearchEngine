from django.shortcuts import render
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['POST'])
def query_book(request):
    if request.method == 'POST':
        print("request.data")
        print(request.data)