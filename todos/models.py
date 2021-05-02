from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categoria(models.Model):
  nome=models.TextField(default="")

class Todo(models.Model):
  titolo=models.TextField(default="")
  descrizione=models.TextField(default="")
  autore=models.ForeignKey(User,on_delete=models.CASCADE)
  categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)
  