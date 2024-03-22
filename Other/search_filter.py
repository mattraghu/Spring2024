import tkinter as tk
from recipe_widget import RecipeWidget
import time 
class DoubleScaleFilter(tk.Frame):
    """A custom widget for double-sided slider."""
    def __init__(self, master, label, from_, to_, default_low, default_high, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.label = tk.Label(self, text=label)
        self.label.pack()

        # Initialize the low scale with the default low value
        self.low_scale = tk.Scale(self, from_=from_, to=to_, orient='horizontal', label='Low')
        self.low_scale.set(default_low)  # Set the default low value
        self.low_scale.pack(side=tk.LEFT)

        # Initialize the high scale with the default high value
        self.high_scale = tk.Scale(self, from_=from_, to=to_, orient='horizontal', label='High')
        self.high_scale.set(default_high)  # Set the default high value
        self.high_scale.pack(side=tk.RIGHT)


    def get_values(self):
        """Returns the low and high values."""
        return {'low': self.low_scale.get(), 'high': self.high_scale.get()}

class SearchFilterFrame(tk.Frame):
    def __init__(self, master, on_search=None, on_filter_change=None, data_manager=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.on_search = on_search
        self.on_filter_change = on_filter_change
        self.data_manager = data_manager
        self.scheduled_event = None  # Attribute to store the reference to the scheduled event
        self.last_search = 0  # To prevent spamming the API
        self.delay = 2000  # Delay in milliseconds


        self.create_widgets()

    def create_widgets(self):
        self.search_entry = tk.Entry(self, width=30)
        self.search_entry.grid(row=0, column=0, padx=10, pady=10)
        self.search_button = tk.Button(self, text="Search", command= lambda: self.schedule_search(True))

        self.search_button.grid(row=0, column=1, padx=10, pady=10)


        #also on key relase search
        self.search_entry.bind("<KeyRelease>", lambda event: self.search())

        
        # Initialize filters frame
        filters_frame = tk.Frame(self, relief='groove', borderwidth=2)
        filters_frame.grid(row=1, column=0, columnspan=2, sticky='ew')

        # Initialize double-sided sliders for filters
        self.filters = {
    'Protein': DoubleScaleFilter(filters_frame, 'Protein', 0, 100, default_low=10, default_high=20),
    'Carbs': DoubleScaleFilter(filters_frame, 'Carbs', 0, 100, default_low=10, default_high=30),
    'Fats': DoubleScaleFilter(filters_frame, 'Fats', 0, 100, default_low=5, default_high=15),
    'Calories': DoubleScaleFilter(filters_frame, 'Calories', 0, 5000, default_low=200, default_high=500)
}


        # Layout filters
        row = 1
        for filter_name, widget in self.filters.items():
            widget.grid(row=row, column=0, columnspan=2, sticky='ew', padx=10, pady=5)
            widget.low_scale.bind("<ButtonRelease-1>", self.filter_change)
            widget.high_scale.bind("<ButtonRelease-1>", self.filter_change)
            row += 1


        # Create a frame to hold the search results
        self.search_results_frame = tk.Frame(self)
        self.search_results_frame.grid(row=2, column=0, columnspan=2, sticky='nsew')
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def update_search_results(self, results):
        # Clear existing search results
        for widget in self.search_results_frame.winfo_children():
            widget.destroy()

        for recipe_name, macros in results.items():
            print(recipe_name)
            widget = RecipeWidget(self.search_results_frame, recipe_name, macros, self.on_recipe_selected)
            widget.pack()


    def schedule_search(self, override=False):
        if self.scheduled_event:
            self.after_cancel(self.scheduled_event)  # Cancel the previous scheduled event if it exists

        if time.time() - self.last_search < self.delay / 1000 and not override:
            self.scheduled_event = self.after(self.delay, self.perform_search)
        else:
            self.perform_search()

    def perform_search(self):
        self.last_search = time.time()
        if self.on_search:
            self.on_search(self.search_entry.get())
        self.scheduled_event = None  # Reset the scheduled event reference

    def search(self):
        self.schedule_search()


    def perform_filter_change(self):
        # Collect the current filter values and invoke the callback with the new format
        if self.on_filter_change:
            filters = {name: widget.get_values() for name, widget in self.filters.items()}
            self.on_filter_change(filters)
        self.scheduled_event = None  # Reset the scheduled event reference

    def filter_change(self, event):
        self.perform_filter_change()


    # This method needs to be added to handle the recipe selection event
    def on_recipe_selected(self, recipe_name, macros):
        self.master.show_recipe_detail(recipe_name, macros)

