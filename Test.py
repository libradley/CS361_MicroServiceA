import json
import os

def create_recipe_data():
    json_path = './recipe.json'

    if os.path.exists(json_path):
        return
    else:
        recipe = {
            'X': {'id': '1', 'version': '1', 'properties': [4, 3]},
            'Y': {'id': '1', 'version': '1', 'properties': [2, 4]},
            'Z': {'id': '1', 'version': '1', 'properties': [1, 3]},
        }
        with open('recipe_data.json', 'w') as outfile:
            json.dump(recipe, outfile)

if __name__ == "__main__":
    create_recipe_data()