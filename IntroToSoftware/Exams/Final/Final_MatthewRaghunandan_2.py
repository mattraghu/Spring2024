class BookStoreInventoryManager:
    def __init__(self):
        print("Inventory Management System")
        self.books = []
        self.commands = [
            ("Add Book" , self.addBook),
            ("Remove Book" , self.removeBook),
            ("Update Quantity" , self.updateQuantity),
            ("Search Book" , self.searchBook),
            ("Exit" , self.exit),
        ]

    def exit(self):
        print("Exiting program.")
        exit()


    def addBook(self):
        title = str(input("Enter title of the book: "))
        author = str(input("Enter author of the book: "))
        genre = str(input("Enter genre of the book: "))
        quantity = str(input("Enter quantity of the book: "))
        if not quantity.isdigit():
            print("Please enter a valid NUMBER for quantity")
            return

        self.books.append([title,author,genre,quantity])

    def removeBook(self):
        name = str(input("Enter the title of the book you want to remove: "))
        for book in self.books:
            if name in book:
                self.books.remove(book)
                print(f"{name} has been removed from the inventory.")

    def updateQuantity(self):
        name = str(input("Enter the title of the book you want to update the quantity for: "))
        for book in self.books:
            if name in book:
                quantity = str(input(f"Enter the new quantity for {book} (old = {book[3]}): "))

                if not quantity.isdigit():
                    print("Please enter a valid NUMBER for quantity")
                    return
                book[3] = quantity

    def searchBook(self):
        name = str(input("Enter the title of the book you want to search for: "))
        for book in self.books:
            if name in book:
                print(f"Title: {book[0]}")
                print(f"Author: {book[1]}")
                print(f"Genre: {book[2]}")
                print(f"Quantity: {book[3]}")


    def loop(self):
        while True:
            print("-------------")
            for i,commandInfo in enumerate(self.commands):
                print(f"{i+1}. {commandInfo[0]}")
            choice = (input("Enter your choice: "))
            if choice.isdigit(): 
                choice = int(choice)
                if choice > 0 and choice <= len(self.commands):
                    self.commands[choice-1][1]()
                else:
                    print("Please enter a valid number.")

            else:
                print("Please enter a NUMBER.")

            



invManager = BookStoreInventoryManager()
invManager.loop()