from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import HttpResponse
from book.models import Book, Words
# Create your views here.

@api_view(['POST'])
def query_book(request):
    if request.method == 'POST':
        print("request.data")
        print(request.data)
    return HttpResponse("Hello World!")

# def find_words(query, k):
