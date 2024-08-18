import json
import re
import nltk
from nltk.corpus import wordnet
from nltk.corpus import stopwords

quantities = ['cup', 'cups', 'teaspoon', 'teaspoons', 'tablespoon', 'tablespoons', 'liter', 'liters', 'ml', 'g', 'grams', 'kg', 'kilograms', 'oz', 'ounce', 'ounces']
states = ['chopped', 'grated', 'boiled', 'finely chopped', 'diced', 'sliced']

# Pattern for quantities and units
quantity_unit_pattern = r'(\d+/\d+|\d+\.\d+|\d+)\s*(cup|cups|teaspoon|teaspoons|tablespoon|tablespoons|liter|liters|ml|g|grams|kg|kilograms|oz|ounce|ounces)'

# Pattern for ingredient states
state_pattern = r'\b(chopped|grated|boiled|finely chopped|diced|sliced)\b'

    
def ExtractIngredients(text):
    """
    Extract ingredients from the recipe steps
    """
    # Extract quantities and units
    quantities_units = re.findall(quantity_unit_pattern, text)
    print(quantities_units)
    # Extract states
    states = re.findall(state_pattern, text)
    print(states)

    # Extract ingredient names by removing matched quantities and states
    ingredient_names = re.sub(quantity_unit_pattern, '', text)
    ingredient_names = re.sub(state_pattern, '', ingredient_names)
    ingredient_names = [name.strip() for name in ingredient_names.split(',') if name.strip()]
    
    # Combine the extracted information
  
    return ingredients