from django.utils import timezone
from django.db import models

class Author(models.Model):
    
    def __str__(self):
        return self.author_name

    gender_choices = [
        ('M', 'Male'),
        ('F', 'Female')
    ]
    salutation = models.CharField(max_length=2)
    author_name = models.CharField(max_length=200)
    gender = models.CharField(max_length=1, choices=gender_choices)
    phone = models.BigIntegerField()

class Book(models.Model):
    def __str__(self):
        return self.book_name

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    book_name = models.CharField(max_length=100)
    edition = models.DecimalField(max_digits=5, decimal_places=2)
    pub_date = models.DateField('date published')
    price = models.FloatField()
    synopsis = models.TextField()