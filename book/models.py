from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=128, null=False)
    author = models.CharField(max_length=128)
    id = models.IntegerField(primary_key=True)

class Words(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    word = models.CharField(max_length=128, null=False)
    count = models.IntegerField()
