import random

class DataManager:
    def __init__(self):
        # In a real application, you might load this data from a database or an API
        self.recipes = {
            'Chicken Salad': {'Protein': 30, 'Carbs': 10, 'Fats': 15, 'Calories': 350},
            'Quinoa & Beans': {'Protein': 15, 'Carbs': 40, 'Fats': 5, 'Calories': 250},
            'Protein Shake': {'Protein': 25, 'Carbs': 5, 'Fats': 2, 'Calories': 180},
            # Add more recipes as needed...
        }

    def search_recipes(self, query):
        # Case insensitive search in recipe names
        print("AHHH")
        return {name: macros for name, macros in self.recipes.items() if query.lower() in name.lower()}

    def filter_recipes(self, filters):
        # Filter recipes based on the macronutrient criteria
        def recipe_matches(recipe, filters):
            return all(recipe.get(macro) <= amount for macro, amount in filters.items())

        return {name: macros for name, macros in self.recipes.items() if recipe_matches(macros, filters)}

    def add_random_recipes(self, count=5):
        # This method would add random recipes to the dictionary for testing purposes
        base_names = ['Salad', 'Stir Fry', 'Soup', 'Pasta', 'Sandwich']
        for _ in range(count):
            name = f"Random {random.choice(base_names)}"
            macros = {
                'Protein': random.randint(10, 40),
                'Carbs': random.randint(10, 60),
                'Fats': random.randint(5, 30),
                'Calories': random.randint(200, 600)
            }
            self.recipes[name] = macros

# Example usage
if __name__ == "__main__":
    data_manager = DataManager()
    data_manager.add_random_recipes()

    # Search test
    search_results = data_manager.search_recipes('Salad')
    print("Search results:", search_results)

    # Filter test
    filter_criteria = {'Protein': 30, 'Carbs': 50, 'Fats': 20, 'Calories': 400}
    filtered_results = data_manager.filter_recipes(filter_criteria)
    print("Filtered results:", filtered_results)
