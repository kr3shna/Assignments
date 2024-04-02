from datetime import datetime, timedelta

class Library:
    def __init__(self):
        self.catalog = {}  # {book_id: [title, author, quantity]}
        self.users = {}  # {user_id: [name, {book_id: [checkout_date, due_date]}]}

    def display_catalog(self):
        print("Catalog:")
        for book_id, details in self.catalog.items():
            print(f"Book ID: {book_id}, Title: {details[0]}, Author: {details[1]}, Quantity available: {details[2]}")

    def register_user(self, user_id, name):
        if user_id not in self.users:
            self.users[user_id] = [name, {}]
            print("User registered successfully.")
        else:
            print("User ID already exists. Please choose another.")

    def checkout_book(self, user_id, book_id):
        if user_id not in self.users:
            print("User not registered.")
            return
        if book_id not in self.catalog:
            print("Book ID not found.")
            return
        if self.catalog[book_id][2] <= 0:
            print("Book not available for checkout.")
            return
        if len(self.users[user_id][1]) >= 3:
            print("User has already checked out 3 books.")
            return

        checkout_date = datetime.now()
        due_date = checkout_date + timedelta(days=14)
        self.users[user_id][1][book_id] = [checkout_date, due_date]
        self.catalog[book_id][2] -= 1
        print("Book checked out successfully.")

    def return_book(self, user_id, book_id):
        if user_id not in self.users:
            print("User not registered.")
            return
        if book_id not in self.users[user_id][1]:
            print("Book not checked out by this user.")
            return

        checkout_date, due_date = self.users[user_id][1].pop(book_id)
        return_date = datetime.now()
        if return_date > due_date:
            days_overdue = (return_date - due_date).days
            fine = days_overdue * 1
            print(f"Book returned successfully. Overdue fine: ${fine}.")
        else:
            print("Book returned successfully.")

        self.catalog[book_id][2] += 1

    def list_overdue_books(self, user_id):
        if user_id not in self.users:
            print("User not registered.")
            return

        total_fine = 0
        print("Overdue Books:")
        for book_id, dates in self.users[user_id][1].items():
            checkout_date, due_date = dates
            if datetime.now() > due_date:
                days_overdue = (datetime.now() - due_date).days
                fine = days_overdue * 1
                print(f"Book ID: {book_id}, Days overdue: {days_overdue}, Fine: ${fine}")
                total_fine += fine

        print(f"Total Fine: ${total_fine}")

# Sample usage
library = Library()
library.catalog = {
    1: ["Book1", "Author1", 2],
    2: ["Book2", "Author2", 1],
    3: ["Book3", "Author3", 3]
}

library.display_catalog()

library.register_user(101, "User1")
library.register_user(102, "User2")

library.checkout_book(101, 1)
library.checkout_book(101, 2)
library.checkout_book(102, 3)

library.return_book(101, 1)
library.return_book(102, 3)

library.list_overdue_books(101)