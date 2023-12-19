from ariadne import QueryType, make_executable_schema, load_schema_from_path, MutationType
from blog import resolvers as blog_resolvers

type_defs = load_schema_from_path("schemas")

query = QueryType()

mutation = MutationType()
mutation.set_field('createAuthor', blog_resolvers.resolve_create_author)
mutation.set_field('postBlog', blog_resolvers.resolve_post_blog)

query.set_field('getBlogs', blog_resolvers.resolve_get_blogs)
query.set_field('getBlog', blog_resolvers.resolve_get_blog)

schema = make_executable_schema(type_defs, mutation, query)