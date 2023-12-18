from .models import Author, Blog

def resolve_create_author(*_, input: dict):
  author = Author.objects.create(username=input['username'], age=input['age'])
  author.save()
  return {
    "message": "Author created",
    "author": author
  }


def resolve_post_blog(*_, input:dict):
  try:
    author = Author.objects.get(username=input['authorUsername'])
    blog = Blog.objects.create(title=input['title'], content=input['content'], author=author)
    blog.save()
    return{
      "message": "Blog posted",
      "blog": blog
    }
  except Author.DoesNotExist:
    raise Exception("Author does not exist")

