import openai

OPENAI_API_KEY = '' # @RU REMOVE BEFORE COMMITING!!! AHHHHHH
openai.api_key = OPENAI_API_KEY

#{"role": "system", "content": "You are an application that takes in an ingredient list for a recipe or a detailed recipe, as well as a list of allergens, and will modify the recipe by taking out the allergy-containing ingredient and replacing it with a viable substitution. Be sure to consider what the recipe is for and if it is sweet or savory when deciding on a viable replacement (for example apple sauce is a bad egg replacment for savory dishes but good for sweet dishes). Results will be in a JSON format, being {{'ingredients':[LIST OF INGREDIENTS], 'recipe':<MODIFIED RECIPE STRING>}}. The ingredients should be displayed in a list, and the modified ingredients should be italicized. Only italicize the ingredients we are using as substitutions, it should not be italisized if it was mentioned in the original inputted recipe. For example, if the original recipe includes flour,chicken, and we replace the chicken with mushrooms, then the output would only italicize mushrooms (as *mushrooms*) but not the flour. This list will be in the 'ingredients' part of the JSON object.You will take in input by first reading in a recipe list and below it will be a string 'Allergies:' followed by a list of allergens. A detailed recipe input would be an input where all the steps of making the food are shared. If a detailed recipe was shared where it explains what to do with the ingredients, then you will also output those recipe ingredients again but now with the modified instructions including the modified ingredient, and this will be placed in the 'instructions' part of the JSON output. Overall the ourput will be the JSON object which has the numbered modified ingredients list, and then a modified recipe instructions ONLY IF recipe instructions were part of the input. If the recipe instructions was not part of thr input then the 'instructions' will be empty in the JSON object. Remember, ingredients are a description of a food item and the quantity of it that is needed. If the input also includes descriiptions on how to use the ingredients, then those are instructions, and they should be part of the 'instructions' area of the JSON file and not in the 'ingredients' area. If the instructions were not provided, then we will not include anything in that section of the JSON object."}


recipe_inputs = ["2 slices of wheat bread, mayonaise, 4 strips of bacon, 2 slices of roma tomato, lettuce"]
allergy_list = ["fish", "tree nuts", "egg", "pork"]

for recipe in recipe_inputs:


    completion = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are an application that takes in an ingredient list of ingredients for a recipe, as well as a list of allergens, and will modify the ingredients by taking out the allergy-containing ingredient and replacing it with a viable substitution. Be sure to consider what the recipe is for and if it is sweet or savory when deciding on a viable replacement (for example apple sauce is a bad egg replacment for savory dishes but good for sweet dishes). When deciding on a viable replacement, weigh options what are more common or accessible for general use more favorably over pther potential solutions. Results will be in a JSON format, being {{'ingredients':[LIST OF INGREDIENTS],'changes':<EXPLANATION HERE>}}. The ingredients should be displayed in a list, and the modified ingredients should be italicized. Only italicize the ingredients we are using as substitutions, it should not be italisized if it was mentioned in the original inputted recipe. For example, if the original recipe includes flour,chicken, and we replace the chicken with mushrooms, then the output would only italicize mushrooms (as *mushrooms*) but not the flour. This list will be in the 'ingredients' part of the JSON object.You will take in input by first reading in a recipe list and below it will be a string 'Allergies:' followed by a list of allergens. Then, you should explain what potential effects the substitution could have on the food item. For example, if eggs are replaced with bananas in a cookie recipe, then the cookies may be sweeter than usual. Place this explanation string inside the 'changes' section in the JSON object. Overall the output will be the JSON object which has the numbered modified ingredients list and an explanation of what potential changes may occur in the recipe with the modifications."}
        ,{"role": "user", "content": f"{recipe}\nAllergies: {','.join(allergy_list)}"}]
    )
    print(completion.choices[0].message["content"])
    print()