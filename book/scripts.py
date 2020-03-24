import json
import codecs
import os
import requests
from book.models import Book, Words, WordCount
import re


#function to parse special characters in the input file
def unmangle_utf8(match):
    escaped = match.group(0)                   # '\\u00e2\\u0082\\u00ac'
    hexstr = escaped.replace(r'\u00a0', '')      # 'e282ac'
    buffer = codecs.decode(hexstr, "hex")      # b'\xe2\x82\xac'

    try:
        return buffer.decode('utf8')           # '€'
    except UnicodeDecodeError:
        print("Could not decode buffer: %s" % buffer)


#function to check if the string has digits
def hasNumbers(inputString):
    return bool(re.search(r'\d', inputString))


def populate_data_prod():
    populate_data('data.json')


def populate_data_test():
    populate_data('data_test.json')

#function to populate and pre process data from the data.json file
#TODO - We can run this job freequently in Airflow DAGs to keep updating our data set
def populate_data(file):
    currentDirectory = os.path.dirname(__file__)
    dataFilePath = os.path.join(currentDirectory, file)
    with open(dataFilePath) as f:
        stringNew = f.read()
        data = json.loads(re.sub(r"(?i)(?:\\u00[0-9a-f]{2})+", unmangle_utf8, stringNew))
        lengthOfData = len(data["titles"])
        print("total is "+str(lengthOfData))
        for i in range(lengthOfData):
            print(i)
            title = data["titles"][i]
            summary = data["summaries"][i]["summary"]
            parts = summary.split(":")
            summary1 = parts[1]
            parts = re.split(r'[;\-,.\s]\s*',summary1)
            titleParts = re.split(r'[;\-,.\s]\s*', title)
            parts.extend(titleParts)
            nonEmptyParts = [part.lower() for part in parts if len(part)>0 and (not hasNumbers(part))]
            dict = {}
            for part in nonEmptyParts:
                if part in dict:
                    dict[part] +=1
                else:
                    dict[part] =1
            id = data["summaries"][i]["id"]
            author = get_author_details(id)
            b = Book(title = title, id = id, summary = summary, author = author)
            b.save()
            for key in dict:
                try:
                    w = Words.objects.get(word = key)
                except:
                    w = Words(word=key)
                    w.save()
                wc = WordCount(book = b, word = w, count = dict[key])
                wc.save()


#returns author name given a book ID
def get_author_details(id):
    url = "https://ie4djxzt8j.execute-api.eu-west-1.amazonaws.com/coding"
    payload = "{\"book_id\": "+str(id)+"}"
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    res = json.loads(response.text.encode('utf8'))
    return res["author"]


#To delete all values in table
def reset_migrations():
    WordCount.objects.all().delete()
    Words.objects.all().delete()
    Book.objects.all().delete()