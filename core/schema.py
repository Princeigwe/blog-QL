from ariadne import QueryType, make_executable_schema, load_schema_from_path, MutationType
from blog import resolvers as blog_resolvers

type_defs = load_schema_from_path("schemas")

query = QueryType()

mutation = MutationType()
mutation.set_field('createAuthor', blog_resolvers.resolve_create_author)

schema = make_executable_schema(type_defs, mutation, query)