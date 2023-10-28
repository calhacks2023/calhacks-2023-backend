import requests

recipe_inputs = ["""Preheat the oven to 350ºF. Grease a 9×5-inch loaf pan with nonstick cooking spray and set aside.
In a medium bowl, whisk together the flour, baking soda, and salt. Set aside.

In a large bowl, mash the ripe bananas with a fork. Add the peanut butter and melted butter and stir until combined. Stir in the brown sugar, egg, and vanilla extract. Stir until smooth.
Stir the dry ingredients into the wet ingredients, don’t over mix.
Pour batter into prepared pan. Bake for 50-65 minutes, or until a toothpick inserted into the center of the bread comes out clean. Check the bread at 50 minutes, just to be safe. Oven times vary.

Remove the pan from the oven and set on a wire cooling rack. Let the bread cool in the pan for 10 minutes. Run a knife around the edges of the bread and carefully remove from the pan. Let the bread cool on the wire cooling rack until slightly warm. Cut into slices and serve.Note-the bread will keep on the counter, wrapped in plastic wrap, for up to 3 days. This bread also freezes well. To freeze, cool the bread completely and wrap in plastic wrap and place in a freezer bag. Freeze for up to 1 month. Defrost before slicing.""",
"""Step 1
Using kitchen twine, tie tenderloin in 4 places. Season generously with salt and pepper.
Step 2
Over high heat, coat bottom of a heavy skillet with olive oil. Once pan is nearly smoking, sear tenderloin until well-browned on all sides, including the ends, about 2 minutes per side (12 minutes total). Transfer to a plate. When cool enough to handle, snip off twine and coat all sides with mustard. Let cool in fridge.
Step 3
Meanwhile, make duxelles: In a food processor, pulse mushrooms, shallots, and thyme until finely chopped.
Step 4
To skillet, add butter and melt over medium heat. Add mushroom mixture and cook until liquid has evaporated, about 25 minutes. Season with salt and pepper, then let cool in fridge.
Step 5
Place plastic wrap down on a work surface, overlapping so that it’s twice the length and width of the tenderloin. Shingle the prosciutto on the plastic wrap into a rectangle that’s big enough to cover the whole tenderloin. Spread the duxelles evenly and thinly over the prosciutto.
Step 6
Season tenderloin, then place it at the bottom of the prosciutto. Roll meat into prosciutto-mushroom mixture, using plastic wrap to roll tightly. Tuck ends of prosciutto as you roll, then twist ends of plastic wrap tightly into a log and transfer to fridge to chill (this helps it maintain its shape).
Step 7
Heat oven to 425°. Lightly flour your work surface, then spread out puff pastry and roll it into a rectangle that will cover the tenderloin (just a little bigger than the prosciutto rectangle you just made!). Remove tenderloin from plastic wrap and place on bottom of puff pastry. Brush the other three edges of the pastry with egg wash, then tightly roll beef into pastry.
Step 8
Once the log is fully covered in puff pastry, trim any extra pastry, then crimp edges with a fork to seal well. Wrap roll in plastic wrap to get a really tight cylinder, then chill for 20 minutes.
Step 9
Remove plastic wrap, then transfer roll to a foil-lined baking sheet. Brush with egg wash and sprinkle with flaky salt.
Step 10
Bake until pastry is golden and the center registers 120°F for medium-rare, about 40 to 45 minutes. Let rest 10 minutes before carving and serving.""",
"""Prepare your food processor. I prefer to use the small bowl attachment that came with our food processor to make mayonnaise.
Add an egg to the bowl of your food processor and process for about 20 seconds.
Add mustard, vinegar, and salt then process for another 20 seconds.
Slowly add the oil, in tiny drops, until about a quarter of the oil has been added. Adding the oil slowly is really important. If you were to dump it all in at once, you’d have mayonnaise soup!
Taste the mayonnaise and adjust with additional salt and vinegar or lemon juice."""]
allergy_list = ["egg", "peanut"]
prompt_formatting = f"A numbered list has the format of 1. ITEM_1 2. ITEM_2 3. ITEM_3"
prompt_allergens = f"I am allergic to {','.join}"
prompt_ingredients = f"Output a numbered list (and nothing else) of the ingredients, substituting the follow {','.join(allergy_list)}, all of which I am allergic to."
prompt_instructions = f"Output a numbered list (and nothing else) of the instructions, providing substitutions for {','.join(allergy_list)}, all of which I am allergic to."

url = "https://api.together.xyz/inference"

for recipe in recipe_inputs:
    payload_ingredients = {
        "model": "togethercomputer/llama-2-13b-chat",
        "prompt": recipe + "\n\n" + prompt_ingredients,
        "max_tokens": 1000
    }
    payload_instructions = {
        "model": "togethercomputer/llama-2-13b-chat",
        "prompt": recipe + "\n\n" + prompt_instructions,
        "max_tokens": 1000
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "Authorization": "Bearer API_KEY_GOES_HERE"
    }

    response_ingredients = requests.post(url, json=payload_ingredients, headers=headers)
    response_instructions = requests.post(url, json=payload_instructions, headers=headers)

    # output
    print("Ingredients Result:")
    print(response_ingredients.json()["output"]["choices"][0]["text"])
    print("Instructions Result:")
    print(response_instructions.json()["output"]["choices"][0]["text"])
    print()
    print("------------------------------------------")
    print()