from pydantic import BaseModel

class RecipeAndRestrictions(BaseModel):
    restrictions: str
    recipe: str