from pydantic import BaseModel

class RecipeAndRestrictions(BaseModel):
    recipe: str
    restrictions: str