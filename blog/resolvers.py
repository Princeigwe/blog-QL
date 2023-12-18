from .models import Author

def resolve_create_author(*_, input: dict):
  author = Author.objects.create(username=input['username'], age=input['age'])
  author.save()
  return {
    "message": "Author created",
    "author": author
  }