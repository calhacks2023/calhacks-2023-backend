from pymilvus import MilvusClient
from langchain.embeddings import HuggingFaceBgeEmbeddings

client = MilvusClient(
    uri="INSERT_ZILLIZ_URI",
    token="INSERT_ZILLIZ_TOKEN"
)

model_name = "BAAI/bge-small-en"
model_kwargs = {'device': 'cpu'}
encode_kwargs = {'normalize_embeddings': True}
hf = HuggingFaceBgeEmbeddings(
    model_name=model_name,
    model_kwargs=model_kwargs,
    encode_kwargs=encode_kwargs
)

def embed_words(words):
    return hf.embed_query(words)

def insert_recipe(recipe, restrictions):
    restrictions_list = restrictions.split(",")
    for r in restrictions_list:
        client.insert(
            collection_name="Recipes",
            data={
                "recipe": recipe,
                "recipe_vector": embed_words(recipe),
                "substitute_for": r
            }
        )

def remove_duplicates(alist):
    seen = set()
    seen_add = seen.add
    return [x for x in alist if not (x in seen or seen_add(x))]

def search_recipe(recipe_vector, restrictions):
    res = []
    output_list = []
    if len(restrictions) == 0:
        res = client.search(
            collection_name="Recipes",
            data = [recipe_vector],
            output_fields=["recipe"])
    else:
        res = client.search(
            collection_name='Recipes',
            data = [recipe_vector],
            output_fields=["recipe"],
            filter=f'substitute_for in {restrictions.split(",")}'
        )

    
    for r in res[0]:
        if r["distance"] >= 0.05: # Similar, but not too similar
            output_list.append(r["entity"]["recipe"])
    
    return remove_duplicates(output_list)