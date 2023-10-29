# Script to run separately from web app (creates a new collection in the database)

from pymilvus import connections, FieldSchema, DataType, CollectionSchema, Collection

connections.connect(
  alias="default", 
  uri="INSERT_ZILLIZ_URI",
  secure=True,
  token="INSERT_ZILLIZ_TOKEN"
)

fields = [
    FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, auto_id=True),
    FieldSchema(name="recipe", dtype=DataType.VARCHAR, max_length=1000),
    FieldSchema(name="recipe_vector", dtype=DataType.FLOAT_VECTOR, dim=384),
    FieldSchema(name="substitute_for", dtype=DataType.VARCHAR, max_length=100)
]

schema = CollectionSchema(
    fields,
    description="",
        enable_dynamic_field=False
)

collection = Collection(
    name="Recipes", 
    description="",
    schema=schema
)

index_params = {
    "index_type": "AUTOINDEX",
    "metric_type": "L2",
    "params": {}
}

collection.create_index(
  field_name="recipe_vector", 
  index_params=index_params,
  index_name='recipe_vector_index'
)

collection.load()