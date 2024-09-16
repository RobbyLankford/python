"""
6.101 Lab 5:
Recipes
"""

import pickle
import sys

sys.setrecursionlimit(20_000)

# NO ADDITIONAL IMPORTS!

def atomic_ingredient_costs(recipes: list[set]) -> dict:
    """
    Given a recipes list, make and return a dictionary mapping each atomic food item
    name to its cost.
    """
    atomic_foods = dict()
    for recipe in recipes:
        type = recipe[0]
        if type == 'atomic':
            food = recipe[1]
            cost = recipe[2]

            atomic_foods[food] = cost
    
    return atomic_foods


def compound_ingredient_possibilities(recipes: list[set]) -> dict:
    """
    Given recipes, a list containing compound and atomic food items, make and
    return a dictionary that maps each compound food item name to a list
    of all the ingredient lists associated with that name.
    """
    foods = dict()
    for recipe in recipes:
        type = recipe[0]
        if type == 'compound':
            food = recipe[1]
            ingredients = recipe[2]

            if food not in foods:
                foods[food] = []
            
            foods[food].append(ingredients)
    
    return foods


def lowest_cost(recipes: list[set], food_item: str, ignore_list: list = None) -> float:
    """
    Given a recipes list and the name of a food item, return the lowest cost of
    a full recipe for the given food item.
    """
    # Using a set results in a faster lookup time
    ignore_set = set(ignore_list) if ignore_list else set()

    # Avoid redundant calculations
    calculated_costs = {}

    # Recursive helper to calculate the lowest cost of a food item
    def find_cost(food):
        # Do not need to calculate if food item is to be ignored
        if food in ignore_set:
            return None

        # Do not need to re-calculate if cost has already been calculated
        if food in calculated_costs:
            return calculated_costs[food]

        # A given food can have multiple recipes
        food_recipes = [recipe for recipe in recipes if recipe[1] == food]

        # Food might not been in recipes list
        if not food_recipes:
            calculated_costs[food] = None
            
            return None

        # Base Case: Atomic Food (uses similar logic to `atomic_ingredient_costs`)
        if food_recipes[0][0] == 'atomic':
            total_cost = food_recipes[0][2]
            calculated_costs[food] = total_cost
            
            return total_cost
        
        # Recursive Case: Compound Food, need to check individual ingredients
        min_cost = float('inf')
        recipe_found = False

        for recipe in food_recipes:
            type = recipe[0]

            if type == 'compound':
                total_cost = 0
                ingredients = recipe[2]
                
                # Check the cost of each ingredient
                for ingredient_name, quantity in ingredients:
                    ingredient_cost = find_cost(ingredient_name)
                    
                    # If any ingredient is missing or ignored, recipe is invalid
                    if ingredient_cost is None:
                        total_cost = None
                        
                        break
                    
                    total_cost += ingredient_cost * quantity
                
                # If the recipe is valid, update the minimum cost
                if total_cost is not None:
                    recipe_found = True
                    min_cost = min(min_cost, total_cost)

        # Possible that no valid recipe is found
        if not recipe_found:
            calculated_costs[food] = None
            return None
        
        # Cache results
        calculated_costs[food] = min_cost
        
        return min_cost
    
    # Run recursive helper function
    return find_cost(food_item)


def scaled_flat_recipe(flat_recipe: dict, n: int) -> dict:
    """
    Given a dictionary of ingredients mapped to quantities needed, returns a
    new dictionary with the quantities scaled by n.
    """
    return {item: quantity * n for item, quantity in flat_recipe.items()}


def add_flat_recipes(flat_recipes: list[dict]) -> dict:
    """
    Given a list of flat_recipe dictionaries that map food items to quantities,
    return a new overall 'grocery list' dictionary that maps each ingredient name
    to the sum of its quantities across the given flat recipes.

    For example,
        add_flat_recipes([{'milk':1, 'chocolate':1}, {'sugar':1, 'milk':2}])
    should return:
        {'milk':3, 'chocolate': 1, 'sugar': 1}
    """
    combined_recipe = {}
    for flat_recipe in flat_recipes:
        for item, quantity in flat_recipe.items():
            if item not in combined_recipe:
                combined_recipe[item] = 0
            
            combined_recipe[item] += quantity
    
    return combined_recipe


def cheapest_flat_recipe(recipes: list[set], food_item: str, ignore_list: list = None) -> dict:
    """
    Given a recipes list and the name of a food item, return a dictionary
    (mapping atomic food items to quantities) representing the cheapest full
    recipe for the given food item.

    Returns None if there is no possible recipe.
    """
    # Using a set results in a faster lookup time
    ignore_set = set(ignore_list) if ignore_list else set()

    # Do not need to re-calculate if already been calculated
    flat_recipes_calculated = {}

    # Recursive helper function to calculate the flat recipe
    def find_flat_recipe(food):
        #> Do not need to calculate if item is to be ignored
        if food in ignore_set:
            return None

        # Do not need to re-calculate if already been calculated
        if food in flat_recipes_calculated:
            return flat_recipes_calculated[food]

        # Find all recipes for the given food
        food_recipes = [recipe for recipe in recipes if recipe[1] == food]

        # Food may be missing from the recipes
        if not food_recipes:
            flat_recipes_calculated[food] = None

            return None

        # Base Case: Atomic Food, return flat recipe with the food item
        if food_recipes[0][0] == 'atomic':
            flat_recipe = {food_recipes[0][1]: 1}
            flat_recipes_calculated[food] = flat_recipe
            
            return flat_recipe

        # Recursive Case: Compound Food, calculate the flat recipe for each valid recipe
        min_cost = float('inf')
        best_flat_recipe = None

        for recipe in food_recipes:
            if recipe[0] == 'compound':
                ingredients = recipe[2]
                flat_recipes = []

                total_cost = 0
                for ingredient_name, quantity in ingredients:
                    ingredient_flat_recipe = find_flat_recipe(ingredient_name)
                    ingredient_cost = lowest_cost(recipes, ingredient_name, ignore_list)

                    # Recipe is invalid if any part of it is forbidden or missing
                    if ingredient_flat_recipe is None or ingredient_cost is None:
                        total_cost = None
                        
                        break

                    total_cost += ingredient_cost * quantity
                    flat_recipes.append(scaled_flat_recipe(ingredient_flat_recipe, quantity))

                # Check if the recipe is the cheapest
                if total_cost is not None and total_cost < min_cost:
                    min_cost = total_cost
                    best_flat_recipe = add_flat_recipes(flat_recipes)

        # Possible that no valid recipe is found
        if best_flat_recipe is None:
            flat_recipes_calculated[food] = None
            
            return None

        # Cache results
        flat_recipes_calculated[food] = best_flat_recipe

        return best_flat_recipe
    
    # Run recursive helper function
    return find_flat_recipe(food_item)


def combined_flat_recipes(flat_recipes: list[list[dict]]) -> list[dict]:
    """
    Given a list of lists of dictionaries, where each inner list represents all
    the flat recipes for a certain ingredient, compute and return a list of flat
    recipe dictionaries that represent all the possible combinations of
    ingredient recipes.
    """
    # Base Case: no lists to combine, return an empty list of combinations
    if not flat_recipes:
        return [{}]

    # Recursive case: Combine the first list with the rest of the lists
    first_list = flat_recipes[0]
    rest_combined = combined_flat_recipes(flat_recipes[1:])

    all_combinations = []

    for recipe in first_list:
        for rest_recipe in rest_combined:
            combined_recipe = add_flat_recipes([recipe, rest_recipe])
            all_combinations.append(combined_recipe)

    return all_combinations


def all_flat_recipes(recipes: list[set], food_item: str, ignore_list: list = None) -> list:
    """
    Given a list of recipes and the name of a food item, produce a list (in any
    order) of all possible flat recipes for that category.

    Returns an empty list if there are no possible recipes
    """
    # Using a set results in a faster lookup time
    ignore_set = set(ignore_list) if ignore_list else set()

    # Avoid redundant calculations
    flat_recipe_calculations = {}

    # Recursive helper function to find all flat recipes
    def find_all_flat_recipes(food):
        # Ignore items in the ignore list
        if food in ignore_set:
            return []

        # Check cache first
        if food in flat_recipe_calculations:
            return flat_recipe_calculations[food]

        # Find all recipes for the given food
        item_recipes = [recipe for recipe in recipes if recipe[1] == food]

        # Base case: Atomic Food, return a list containing one flat recipe
        if item_recipes and item_recipes[0][0] == 'atomic':
            atomic_recipe = {item_recipes[0][1]: 1}
            flat_recipe_calculations[food] = [atomic_recipe]
            
            return [atomic_recipe]

        # Recursive Case: Compound Food
        all_flat_recipes_for_item = []

        for recipe in item_recipes:
            if recipe[0] == 'compound':
                ingredients = recipe[2]
                all_ingredient_flat_recipes = []

                for ingredient_name, quantity in ingredients:
                    ingredient_flat_recipes = find_all_flat_recipes(ingredient_name)

                    # Skip recipe if any ingredient cannot be created
                    if not ingredient_flat_recipes:
                        all_ingredient_flat_recipes = []
                        
                        break

                    # Scale the ingredient flat recipes
                    scaled_recipes = [scaled_flat_recipe(r, quantity) for r in ingredient_flat_recipes]
                    all_ingredient_flat_recipes.append(scaled_recipes)

                # Combine all valid ingredient flat recipes
                if all_ingredient_flat_recipes:
                    combined_recipes = combined_flat_recipes(all_ingredient_flat_recipes)
                    all_flat_recipes_for_item.extend(combined_recipes)

        # Cache results
        flat_recipe_calculations[food] = all_flat_recipes_for_item

        return all_flat_recipes_for_item

    # Run recursive helper function
    return find_all_flat_recipes(food_item)


if __name__ == "__main__":
    pass
