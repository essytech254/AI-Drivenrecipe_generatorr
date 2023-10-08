class Ingredient:
    def __init__(self, name, dietary_restrictions):
        self.name = name
        self.dietary_restrictions = dietary_restrictions

class Recipe:
    def __init__(self, name, ingredients, instructions, dietary_restrictions):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions
        self.dietary_restrictions = dietary_restrictions

class User:
    def __init__(self, name, dietary_preferences):
        self.name = name
        self.dietary_preferences = dietary_preferences

# Store instances of ingredients in a dictionary with the ingredient name as the key
ingredients_db = {
    "salt": Ingredient("salt", []),
    "chicken": Ingredient("chicken", ["gluten-free"]),
    "rice": Ingredient("rice", ["cholesterol-free"])
    # Add more ingredients
}

# Store instances of recipes in a list
recipes_db = [
    Recipe("Chicken Stir-Fry", ["chicken", "soy sauce", "vegetables"], "Instructions...", ["gluten-free"]),
    Recipe("Spaghetti Carbonara", ["spaghetti", "eggs", "bacon"], "Instructions...", ["pork-free"]),
    Recipe("Jollof Rice", ["rice", "bananas", "beef"], "Instructions...", ["cholesterol-free"]),
    # Add more recipes
]

def generate_recipe(user, available_ingredients):
    suitable_recipes = []

    for recipe in recipes_db:
        if all(ingredient in available_ingredients for ingredient in recipe.ingredients) and all(
                pref in user.dietary_preferences for pref in recipe.dietary_restrictions):
            suitable_recipes.append(recipe)

    if not suitable_recipes:
        raise Exception("No suitable recipes found. Please adjust your preferences or available ingredients.")

    # Implement a selection algorithm to choose a recipe from suitable_recipes
    selected_recipe = suitable_recipes[0]

    return selected_recipe

# Create a user instance with dietary preferences
user1 = User("Jenna", ["pork-free", "gluten-free"])

# Specify available ingredients
available_ingredients = ["chicken", "soy sauce", "vegetables"]

# Call the generate_recipe function
selected_recipe = generate_recipe(user1, available_ingredients)

# Print the selected recipe
print("Selected Recipe:")
print("Name:", selected_recipe.name)
print("Ingredients:", selected_recipe.ingredients)
print("Instructions:", selected_recipe.instructions)
print("Dietary Restrictions:", selected_recipe.dietary_restrictions)
