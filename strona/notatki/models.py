from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    tytul = models.CharField(max_length=200)
    tresc = models.TextField()
    priorytet = models.IntegerField(default=0)
    data_utworzenia = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.tytul
