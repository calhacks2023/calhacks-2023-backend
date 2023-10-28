from fastapi import FastAPI
import uvicorn
from models import RecipeAndRestrictions

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/submitrecipe")
async def submit_recipe(recipe: RecipeAndRestrictions):
    return {'recipe': recipe.recipe, 'restrictions': recipe.restrictions}
    

# For deployment on Render
if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=10000)