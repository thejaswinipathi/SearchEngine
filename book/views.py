from rest_framework.decorators import api_view, renderer_classes
from book.models import *
import re
from book.scripts import hasNumbers
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response


# API for task1
# It returns results in the form of a list of dictonaries
# Sample input to the POST request API
#API call - http://127.0.0.1:8000/book/getInfo/
#JSON Body
# {
# 	"query": "i wish there is a change",
# 	"k":3
# }
@api_view(['POST'])
@renderer_classes([JSONRenderer])
def query_book(request):
    resultList = []
    if request.method == 'POST':
        query =request.data["query"]
        k = request.data["k"]
        result = find_words(query, k)
        for item in result:
            dict = {}
            dict["summary"] = Book.objects.get(id = item).summary
            dict["id"] = item
            resultList.append(dict)
    return Response(resultList)


#API for task2
#API to return a list of list of dictonaries
# Sample input to the POST request API
#API call - http://127.0.0.1:8000/book/getInfoList/
#JSON Body
# {
# 	"queries": ["my life change", "i love coding"],
# 	"k":3
# }
#TODO - We can use rest serializer and deserializers
#TODO - We can cache results if we get similar queries, we can return the same response
@api_view(['POST'])
@renderer_classes([JSONRenderer])
def query_book_list(request):
    if request.method == 'POST':
        queries =request.data["queries"]
        k = request.data["k"]
        totalResult = []
        for query in queries:
            resultList = []
            result = find_words(query, k)
            for item in result:
                dict = {}
                dict["summary"] = Book.objects.get(id = item).summary
                dict["id"] = item
                dict["author"] = Book.objects.get(id = item).author
                dict["query"] = query
                resultList.append(dict)
            if len(resultList) !=0:
                totalResult.append(resultList)
    return Response(totalResult)


#function which returns the Book IDs of top k matches of the query
# TODO - can be enhanced to search words using the concept of edit distance, where if we have a word like changes
# TODO - the same can be matched with change, changing, etc..
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
        topK.append(key)
        if (i==k):
            break
    return(topK)