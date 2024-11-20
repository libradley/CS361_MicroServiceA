import json
import os
import matplotlib.pyplot as plot


def load_data(filepath="recipe_data.json"):
    """Loads data from a JSON file."""
    try:
        with open(filepath, "r") as recipe:
            return json.load(recipe)
    except FileNotFoundError:
        return []


recipe = load_data()
user_input = input("Select 0 for density or 1 for thermal expansion:")
if user_input == '0':
    categories = []
    density = []
    for item in recipe.keys():
        name = str(item)
        categories.append(name + '-' + recipe[item]['id'] + ' Ver' + recipe[item]['version'])

    for item in recipe.keys():
        density.append(recipe[item]['properties'][0])
    fig = plot.figure(figsize=(10, 5))
    color = input("Please choose bar color: ")
    plot.bar(categories, density, color=color, width=0.4)

    plot.xlabel("Recipes")
    plot.ylabel("Density Values")
    plot.title("Recipes Vs. Density Values")
    plot.savefig(input("Save figure as:"))

if user_input == '1':
    categories1 = []
    thermal = []
    for item in recipe.keys():
        name = str(item)
        categories1.append(recipe[item]['id'] + '-' + name + ' Ver' + recipe[item]['version'])

    for item in recipe.keys():
        thermal.append(recipe[item]['properties'][1])
    fig = plot.figure(figsize=(10, 5))
    color = input("Please choose bar color: ")
    plot.bar(categories1, thermal, color=color, width=0.4)

    plot.xlabel("Recipes")
    plot.ylabel("Thermal Values")
    plot.title("Recipes Vs. Thermal Values")
    plot.savefig(input("Save figure as:"))