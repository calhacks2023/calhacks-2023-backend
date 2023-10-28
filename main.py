from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from models import RecipeAndRestrictions

app = FastAPI()

# Configure CORS to allow requests from your React application's origin
app.add_middleware(CORSMiddleware,allow_origins=["http://localhost:5173"],allow_credentials=True,allow_methods=["*"],allow_headers=["*"],)

@app.get("/")
async def root(request: Request):
    #return {"message": "Hello World"}
    param1 = request.query_params.get('param1')
    param2 = request.query_params.get('param2')

    print("WE GOT:",param1, param2)


    # Use param1 and param2 as needed
    return {"message": f"Received param1: {param1}, param2: {param2}"}

@app.post("/submitrecipe")
async def submit_recipe(recipe: RecipeAndRestrictions):
    return {'recipe': recipe.recipe, 'restrictions': recipe.restrictions}
    

# For deployment on Render
if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=10000)