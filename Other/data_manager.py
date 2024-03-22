import random
import requests

class DataManager:
    def __init__(self):
        self.api_id, self.api_key = self.load_api_credentials('api_keys.txt')
        self.base_endpoint = 'https://trackapi.nutritionix.com/v2/natural/nutrients'
        self.last_search = 0 # To prevent spamming the API
        self.current_results = {}

    def load_api_credentials(self, filepath):
        # with open(filepath) as f:
        #     api_keys = f.readlines()
        #     app_id = api_keys[0].strip()
        #     api_key = api_keys[1].strip()
        app_id = '4de04e80' #yolo 
        api_key = '007fb7dfa20496b0f06caa06f1440308'
        return app_id, api_key
    
    def fetch_nutrients(self, food_query):
        headers = {
            'x-app-id': self.api_id,
            'x-app-key': self.api_key
        }
        response = requests.post(self.base_endpoint, headers=headers, json={'query': food_query})
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to get nutritional information for {food_query}")
            return None


    def search_recipes(self, query):
        nutrients = self.fetch_nutrients(query)
        if nutrients and 'foods' in nutrients:
            # Process the nutrients response to fit the application's recipe format
            recipes = {}
            for food in nutrients['foods']:
                recipes[food['food_name'].title()] = {
                    'Protein': food['nf_protein'],
                    'Carbs': food['nf_total_carbohydrate'],
                    'Fats': food['nf_total_fat'],
                    'Calories': food['nf_calories']
                }
            self.current_results = recipes
        else:
            self.current_results = {}
        return self.current_results


    # def search_recipes(self, query):
    #     # Case insensitive search in recipe names
    #     return {name: macros for name, macros in self.recipes.items() if query.lower() in name.lower()}

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

