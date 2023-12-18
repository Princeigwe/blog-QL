from django.db import models

# Create your models here.


class Author(models.Model):
  username = models.CharField(max_length=20, unique=True, default="")
  age = models.PositiveIntegerField()

  def __str__(self) -> str:
    return self.name