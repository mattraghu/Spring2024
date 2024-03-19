import tkinter as tk

class RecipeDetailFrame(tk.Frame):
    def __init__(self, master, recipe_name, macros, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.recipe_name = recipe_name
        self.macros = macros

        self.create_widgets()

    def create_widgets(self):
        # Delete any existing widgets
        for widget in self.winfo_children():
            widget.destroy()
        
        # Display the recipe name as a title
        title = tk.Label(self, text=self.recipe_name, font=("Helvetica", 18, "bold"))
        title.pack(pady=10)

        if self.macros:
            # Create a text widget to show the macros information
            text_info = tk.Text(self, height=10, width=50)
            text_info.insert(tk.END, f"Protein: {self.macros['Protein']}g\n")
            text_info.insert(tk.END, f"Carbs: {self.macros['Carbs']}g\n")
            text_info.insert(tk.END, f"Fats: {self.macros['Fats']}g\n")
            text_info.insert(tk.END, f"Calories: {self.macros['Calories']} kcal\n")
            text_info.config(state="disabled")  # Make the text widget read-only
            text_info.pack(pady=10)

        # Button to go back to the search results
        back_button = tk.Button(self, text="Back", command=self.master.show_search_filter)
        back_button.pack(pady=10)

    def update_info(self, recipe_name, macros):
        # Update the displayed information
        self.recipe_name = recipe_name
        self.macros = macros
        self.create_widgets()
