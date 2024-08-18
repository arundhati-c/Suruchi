import json

def ImportRecipeJson(PATH):
    """
    Import a recipe from a JSON file
    """
    with open(PATH, 'r', encoding='utf-8') as file:
        recipe = json.load(file)
    return recipe