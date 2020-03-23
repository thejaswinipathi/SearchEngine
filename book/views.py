from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import HttpResponse
from book.models import *
import re
from book.scripts import hasNumbers


@api_view(['POST'])
def query_book(request):
    if request.method == 'POST':
        print("request.data")
        print(request.data)
    return HttpResponse("Hello World!")


def find_words(query, k):
    parts = re.split(r'[;\-,.\s]\s*', query)
    nonEmptyParts = [part.lower() for part in parts if len(part) > 0 and (not hasNumbers(part))]
    setParts = set(nonEmptyParts)
    dict = {}
    w = []
    for part in setParts:
        try:
            w.append(Words.objects.get(word = part))
        except:
            pass
    if len(w) == 0:
        return []

    wcList = WordCount.objects.filter(word__in = w)
    for wc in wcList:
        bookID = wc.book.id
        count = wc.count
        if bookID in dict:
            dict[bookID] += count
        else:
            dict[bookID] = count
    sortedDict = {k: v for k, v in sorted(dict.items(), key=lambda item: item[1], reverse = True)}
    i = 0
    topK = []
    for key in sortedDict:
        i+=1
        dict = {}
        dict["summary"] = Book.objects.get(id = key).summary
        dict["id"] = key
        topK.append(dict)
        if (i==k):
            break
    print(topK)