from ImportRecipe import ImportRecipeJson
from ExtractIngredients import ExtractIngredients
FILE_PATH = "C:\\Github\\MERNCRUD\\pythonservices\\DummyRecipeHeader.json"

recipe = ImportRecipeJson(FILE_PATH)

for step in recipe['steps']:
    ingredients = ExtractIngredients(step)
    print(ingredients)