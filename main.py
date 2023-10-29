from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.testclient import TestClient
import uvicorn
from models import RecipeAndRestrictions
import openai
import json
import APIKEY #place your api key in a seperate APIKEY.py file as object 'api_key'

OPENAI_API_KEY = APIKEY.api_key # @RU REMOVE BEFORE COMMITING!!! AHHHHHH
openai.api_key = OPENAI_API_KEY

app = FastAPI()

# Configure CORS to allow requests from your React application's origin
app.add_middleware(CORSMiddleware,allow_origins=["http://localhost:5173"],allow_credentials=True,allow_methods=["*"],allow_headers=["*"],)

@app.get("/")
async def root(request: Request):
    #return {"message": "Hello World"}



    # Use param1 and param2 as needed
    return {"message":f"hewo"}

@app.post("/submitrecipe")
async def submit_recipe(recipe: RecipeAndRestrictions):
    completion = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are an application that takes in an ingredient list of ingredients for a recipe, as well as a list of allergens, and will modify the ingredients by taking out the allergy-containing ingredient and replacing it with a viable substitution. Be sure to consider what the recipe is for and if it is sweet or savory when deciding on a viable replacement (for example apple sauce is a bad egg replacment for savory dishes but good for sweet dishes). When deciding on a viable replacement, weigh options what are more common or accessible for general use more favorably over pther potential solutions. Results will be in a JSON format, being {{'ingredients':'INGREDIENT,INGREDIENT,INGREDIENT...','changes':<EXPLANATION HERE>}}. The ingredients should be displayed in a list, and the modified ingredients should be italicized. Only italicize the ingredients we are using as substitutions, it should not be italisized if it was mentioned in the original inputted recipe. For example, if the original recipe includes flour,chicken, and we replace the chicken with mushrooms, then the output would only italicize mushrooms (as *mushrooms*) but not the flour. This list will be in the 'ingredients' part of the JSON object.You will take in input by first reading in a recipe list and below it will be a string 'Allergies:' followed by a list of allergens. Then, you should explain what potential effects the substitution could have on the food item. For example, if eggs are replaced with bananas in a cookie recipe, then the cookies may be sweeter than usual. Place this explanation string inside the 'changes' section in the JSON object. Overall the output will be the JSON object which has the numbered modified ingredients list and an explanation of what potential changes may occur in the recipe with the modifications."}
        ,{"role": "user", "content": f"{recipe.recipe}\nAllergies: {recipe.restrictions}"}]
    )
    #print(completion.choices[0].message["content"])

    json_object = json.loads(completion.choices[0].message["content"])    
    return json_object




# client = TestClient(app) #TESTING

# data = {
#     "recipe": "2 slices of wheat bread, mayonaise, 4 strips of bacon, 2 slices of roma tomato, lettuce",
#     "restrictions": "Egg"
# }

# response = client.post("/submitrecipe", json=data)

# print(response.json())

# For deployment on Render
if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=10000)