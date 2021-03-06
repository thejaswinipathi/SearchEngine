from django.db import models


#TODO - Models can be stored in a NOSQL database, instead of SQLLite
class Book(models.Model):
    title = models.CharField(max_length=128, null=False)
    summary = models.CharField(max_length=128, null=False)
    author = models.CharField(max_length=128)
    id = models.IntegerField(primary_key=True, null=False)


class Words(models.Model):
    word = models.CharField(max_length=128, null=False)


#class to store the number of times a word occured in a book summary
class WordCount(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE, null=False)
    word = models.ForeignKey('Words', on_delete=models.CASCADE, null=False)
    count = models.IntegerField( null=False)