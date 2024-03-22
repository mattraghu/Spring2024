import tkinter as tk
from recipe_widget import RecipeWidget

class SearchFilterFrame(tk.Frame):
    def __init__(self, master, on_search=None, on_filter_change=None, data_manager=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.on_search = on_search
        self.on_filter_change = on_filter_change
        self.data_manager = data_manager

        self.create_widgets()

    def create_widgets(self):
        self.search_entry = tk.Entry(self, width=30)
        self.search_entry.grid(row=0, column=0, padx=10, pady=10)
        self.search_button = tk.Button(self, text="Search", command=self.search)
        self.search_button.grid(row=0, column=1, padx=10, pady=10)


        #also on key relase search
        self.search_entry.bind("<KeyRelease>", lambda event: self.search())

        
        # Create a frame for macro filter sliders
        filters_frame = tk.Frame(self, relief='groove', borderwidth=2)
        filters_frame.grid(row=1, column=0, columnspan=2, sticky='ew')

        # Filter Sliders
        self.filters = {
            'Protein': tk.Scale(filters_frame, from_=0, to=100, orient='horizontal', label='Protein'),
            'Carbs': tk.Scale(filters_frame, from_=0, to=100, orient='horizontal', label='Carbs'),
            'Fats': tk.Scale(filters_frame, from_=0, to=100, orient='horizontal', label='Fats'),
            'Calories': tk.Scale(filters_frame, from_=0, to=5000, orient='horizontal', label='Calories')
        }
        row = 1
        for filter_name, slider in self.filters.items():
            slider.grid(row=row, column=0, columnspan=2, sticky='ew', padx=10, pady=5)
            slider.bind("<ButtonRelease-1>", self.filter_change)
            row += 1


        # Create a frame to hold the search results
        self.search_results_frame = tk.Frame(self)
        self.search_results_frame.grid(row=2, column=0, columnspan=2, sticky='nsew')
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def search(self):
        if self.on_search:
            self.on_search(self.search_entry.get())

    def filter_change(self, event):
        if self.on_filter_change:
            filters = {name: slider.get() for name, slider in self.filters.items()}
            self.on_filter_change(filters)
    def update_search_results(self, results):
        # Clear existing search results
        for widget in self.search_results_frame.winfo_children():
            widget.destroy()

        for recipe_name, macros in results.items():
            print(recipe_name)
            widget = RecipeWidget(self.search_results_frame, recipe_name, macros, self.on_recipe_selected)
            widget.pack()

    # This method needs to be added to handle the recipe selection event
    def on_recipe_selected(self, recipe_name, macros):
        self.master.show_recipe_detail(recipe_name, macros)

