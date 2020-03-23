from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=128, null=False)
    summary = models.CharField(max_length=128, null=False)
    author = models.CharField(max_length=128)
    id = models.IntegerField(primary_key=True, null=False)


class Words(models.Model):
    word = models.CharField(max_length=128, null=False)


class WordCount(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE, null=False)
    word = models.ForeignKey('Words', on_delete=models.CASCADE, null=False)
    count = models.IntegerField( null=False)