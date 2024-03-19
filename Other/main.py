import tkinter as tk
from login import submit_number  # Assuming login.py exists with a function to handle login submission
from search_filter import SearchFilterFrame  # Assuming search_filter.py exists with the SearchFilterFrame class
from recipe_detail import RecipeDetailFrame  # Assuming recipe_detail.py exists with the RecipeDetailFrame class
# from macro_count import MacroCountFrame  # Assuming macro_count.py exists with the MacroCountFrame class
from data_manager import DataManager  # Assuming data_manager.py exists managing data

class MacroCounterApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("EASY MACROS")
        self.geometry("800x600")  # Adjust the size as needed for your design
        
        # Initialize the data manager
        self.data_manager = DataManager()

        # Create the login frame (for the example, we'll skip straight to search/filter)
        # self.login_frame = LoginFrame(self, on_login_success=self.show_search_filter)
        # self.login_frame.pack(fill='both', expand=True)

        # Create the search filter frame
        self.search_filter_frame = SearchFilterFrame(self, on_search=self.perform_search, on_filter_change=self.apply_filters)
        self.search_filter_frame.pack(fill='both', expand=True)

        self.recipe_detail_frame = RecipeDetailFrame(self, "", {})


        # Create the macro count frame (hidden for now)
        # self.macro_count_frame = MacroCountFrame(self)
        # self.macro_count_frame.pack(fill='both', expand=True)
        # self.macro_count_frame.hide()

    def show_recipe_detail(self, recipe_name, macros):
        # Hide other frames and show the recipe detail frame
        self.search_filter_frame.pack_forget()
        self.recipe_detail_frame.update_info(recipe_name, macros)
        self.recipe_detail_frame.pack(fill='both', expand=True)

    # Function to show the search filter screen
    def show_search_filter(self):
        # Hide other frames and show the search filter frame
        # self.login_frame.pack_forget()
        self.recipe_detail_frame.pack_forget()
        self.search_filter_frame.pack(fill='both', expand=True)

    # Function to handle searches from the search filter frame
    def perform_search(self, query):
        results = self.data_manager.search_recipes(query)
        self.search_filter_frame.update_search_results(results)
        pass

    # Function to apply filters from the search filter frame
    def apply_filters(self, filters):
        filtered_results = self.data_manager.filter_recipes(filters)
        self.search_filter_frame.update_search_results(filtered_results)
        pass

    # Function to show the macro count screen
    # def show_macro_count(self):
        # self.search_filter_frame.pack_forget()
        # self.macro_count_frame.show()

if __name__ == "__main__":
    app = MacroCounterApp()
    app.mainloop()

