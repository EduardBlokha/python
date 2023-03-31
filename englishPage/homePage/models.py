from django.db import models
from django.contrib.auth.models import User


class PostModel(models.Model):

    class Marks(models.TextChoices):
        A = 'A'
        B = 'B'
        C = 'C'
        D = 'D'
        E = 'E'
        N = 'No mark'


    title_book = models.CharField(max_length=100)
    content_book = models.TextField()
    translate_book = models.TextField()
    mark_of_translate = models.CharField(
        max_length=7,
        choices=Marks.choices,
        default=Marks.N,
    )
    author = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title_book

class DictionaryModel (models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    translate_book = models.TextField(help_text="Enter words and translation")