from django.db import models

# Create your models here.


class Author(models.Model):
  username = models.CharField(max_length=20, unique=True, default="")
  age = models.PositiveIntegerField()

  def __str__(self) -> str:
    return self.name


class Blog(models.Model):
  title = models.CharField(max_length=20)
  content = models.TextField()
  author = models.ForeignKey(Author, on_delete=models.CASCADE)

  def __str__(self) -> str:
    return self.title