import tkinter as tk

class RecipeWidget(tk.Button):
    def __init__(self, master, recipe_name, macros, on_click, *args, **kwargs):
        super().__init__(master, text=recipe_name, command=lambda: on_click(recipe_name, macros), *args, **kwargs)
        self.recipe_name = recipe_name
        self.macros = macros
        self.on_click = on_click

        self.create_widgets()

    def create_widgets(self):
        self.config(text=f"{self.recipe_name}\nProtein: {self.macros['Protein']}g\n"
                         f"Carbs: {self.macros['Carbs']}g\n"
                         f"Fats: {self.macros['Fats']}g\n"
                         f"Calories: {self.macros['Calories']} kcal")

