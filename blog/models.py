from django.db import models

# Create your models here.


class Author(models.Model):
  name = models.CharField(max_length=20)
  age = models.PositiveIntegerField()

  def __str__(self) -> str:
    return self.name