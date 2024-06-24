import re
from book import Book
from user import User
from author import Author



class LibraryManagementSystem:
    def __init__(self):
        self.books = []
        self.users = []
        self.authors = []

    def main_menu(self):
        while True:
            print("\nWelcome to the Library Management System!\n")
            print("Main Menu:")
            print("1. Book Operations")
            print("2. User Operations")
            print("3. Author Operations")
            print("4. Quit")
            choice = input("Please select an option: ")

            if choice == "1":
                self.book_operations()
            elif choice == "2":
                self.user_operations()
            elif choice == "3":
                self.author_operations()
            elif choice == "4":
                print("Thank you for using the Library Management System. Goodbye!")
                break
            else:
                print("Invalid option, please try again.")

    def book_operations(self):
        while True:
            print("\nBook Operations:")
            print("1. Add a new book")
            print("2. Borrow a book")
            print("3. Return a book")
            print("4. Search for a book")
            print("5. Display all books")
            print("6. Return to Main Menu")
            choice = input("Please select an option: ")

            if choice == "1":
                self.add_new_book()
            elif choice == "2":
                self.borrow_book()
            elif choice == "3":
                self.return_book()
            elif choice == "4":
                self.search_for_book()
            elif choice == "5":
                self.display_all_books()
            elif choice == "6":
                break
            else:
                print("Invalid option, please try again.")
    def add_new_book(self):
        title = input("Enter the title of the book: ")
        author_name = input("Enter the name of the author: ")
        genre = input("Enter the genre of the book: ")
        publication_date = input("Enter the publication date of the book (YYYY-MM-DD): ")

        # Check if the publication date is in the correct format
        if not re.match(r"\d{4}-\d{2}-\d{2}", publication_date):
            print("Invalid date format. Please use the format YYYY-MM-DD.")
            return

        # Check if the author already exists
        author = None
        for a in self.authors:
            if a.name == author_name:
                author = a
                break

        # If the author does not exist, create a new author
        if author is None:
            author_biography = input("Enter the biography of the author: ")
            author = Author(author_name, author_biography)
            self.authors.append(author)

        # Create a new book object
        book = Book(title, author, genre, publication_date)
        self.books.append(book)
        print("Book added successfully!")

    def borrow_book(self):
        title = input("Enter the title of the book you want to borrow: ")
        for book in self.books:
            if book["title"].lower() == title.lower() and not book["is_borrowed"]:
                book["is_borrowed"] = True
                print(f"You have borrowed '{title}'.")
                return
        print("Book is not available.")

    def return_book(self):
        title = input("Enter the title of the book you are returning: ")
        for book in self.books:
            if book["title"].lower() == title.lower() and book["is_borrowed"]:
                book["is_borrowed"] = False
                print(f"Thank you for returning '{title}'.")
                return
        print("This book was not borrowed or does not belong to our library.")

    def search_for_book(self):
        query = input("Enter a search query: ").lower()
        found_books = [book for book in self.books if query in book["title"].lower()]
        if found_books:
            print("Found books:")
            for book in found_books:
                print(f"- {book['title']} by {book['author']} ({'Borrowed' if book['is_borrowed'] else 'Available'})")
        else:
            print("No books found matching your query.")

    def display_all_books(self):
        if not self.books:
            print("No books in the library.")
            return
        print("Library Books:")
        for book in self.books:
            print(f"- {book['title']} by {book['author']} ({'Borrowed' if book['is_borrowed'] else 'Available'})")

    def user_operations(self):
        while True:
            print("\nUser Operations:")
            print("1. Add a new user")
            print("2. Update user information")
            print("3. Delete a user")
            print("4. List all users")
            print("5. Return to main menu")
            choice = input("Please select an option: ")
            if choice == "1":
                self.add_new_user()
            elif choice == "2":
                self.update_user_information()
            elif choice == "3":
                self.delete_user()
            elif choice == "4":
                self.list_all_users()
            elif choice == "5":
                break
            else:
                print("Invalid option, please try again.")
    def add_new_user(self):
        user_id = input("Enter user ID: ")
        name = input("Enter user's name: ")
        email = input("Enter user's email: ")
        self.users.append({
            "user_id": user_id,
            "name": name,
            "email": email
        })
        print(f"User '{name}' added successfully.")

    def update_user_information(self):
        user_id = input("Enter user ID to update: ")
        for user in self.users:
            if user["user_id"] == user_id:
                new_name = input("Enter new name (leave blank to keep current): ")
                new_email = input("Enter new email (leave blank to keep current): ")
                if new_name:
                    user["name"] = new_name
                if new_email:
                    user["email"] = new_email
                print("User information updated successfully.")
                return
        print("User not found.")

    def delete_user(self):
        user_id = input("Enter user ID to delete: ")
        for i, user in enumerate(self.users):
            if user["user_id"] == user_id:
                del self.users[i]
                print("User deleted successfully.")
                return
        print("User not found.")

    def list_all_users(self):
        if not self.users:
            print("No users found.")
            return
        print("List of Users:")
        for user in self.users:
            print(f"- ID: {user}")

    def author_operations(self):
        while True:
            print("\nAuthor Operations:")
            print("1. Add a new author")
            print("2. Update author information")
            print("3. Delete an author")
            print("4. List all authors")
            print("5. Return to main menu")
            choice = input("Please select an option: ")
            if choice == "1":
                self.add_new_author()
            elif choice == "2":
                self.update_author_information()
            elif choice == "3":
                self.delete_author()
            elif choice == "4":
                self.list_all_authors()
            elif choice == "5":
                break
            else:
                print("Invalid option, please try again.")

    def add_new_author(self):
        author_id = input("Enter author ID: ")
        name = input("Enter author's name: ")
        self.authors.append({
            "author_id": author_id,
            "name": name
        })
        print(f"Author '{name}' added successfully.")

    def update_author_information(self):
        author_id = input("Enter author ID to update: ")
        for author in self.authors:
            if author["author_id"] == author_id:
                new_name = input("Enter new name (leave blank to keep current): ")
                if new_name:
                    author["name"] = new_name
                print("Author information updated successfully.")
                return
        print("Author not found.")

    def delete_author(self):
        author_id = input("Enter author ID to delete: ")
        for i, author in enumerate(self.authors):
            if author["author_id"] == author_id:
                del self.authors[i]
                print("Author deleted successfully.")
                return
        print("Author not found.")

    def list_all_authors(self):
        if not self.authors:
            print("No authors found.")
            return
        print("List of Authors:")
        for author in self.authors:
            print(f"- ID: {author['author_id']}, Name: {author['name']}")


if __name__ == "__main__":
    lms = LibraryManagementSystem()
    lms.main_menu()