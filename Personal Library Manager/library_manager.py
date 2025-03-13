def show_menu():
    print("\nWelcome to the Library Manager!")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Update a book")
    print("4. View library stats")
    print("5. List all books")
    print("6. Search for a book")
    print("7. Exit")

def add_book(library, next_book_id):
    title = input("Enter book title: ").strip()
    author = input("Enter author's name: ").strip()
    
    try:
        published_year = int(input("Enter published year: ").strip())
    except ValueError:
        print("Invalid year! Please enter a number.")
        return library, next_book_id

    genre = input("Enter book genre: ").strip()
    read_status = input("Have you read it? (read/unread): ").strip().lower()

    new_book = {
        "id": next_book_id,
        "title": title,
        "author": author,
        "published_year": published_year,
        "genre": genre,
        "read_status": read_status
    }
    
    library.append(new_book)
    print(f"Book '{title}' added successfully!")
    return library, next_book_id + 1

def remove_book(library):
    try:
        book_id = int(input("Enter the book ID to remove: ").strip())
    except ValueError:
        print("Invalid ID! Please enter a number.")
        return library

    new_library = [book for book in library if book["id"] != book_id]
    
    if len(new_library) == len(library):
        print("Book not found.")
    else:
        print("Book removed successfully!")
    
    return new_library

def update_book(library):
    try:
        book_id = int(input("Enter the book ID to update: ").strip())
    except ValueError:
        print("Invalid ID! Please enter a number.")
        return library

    for book in library:
        if book["id"] == book_id:
            title = input(f"New title (press Enter to keep '{book['title']}'): ").strip() or book["title"]
            author = input(f"New author (press Enter to keep '{book['author']}'): ").strip() or book["author"]
            
            try:
                published_year = input(f"New published year (press Enter to keep '{book['published_year']}'): ").strip()
                published_year = int(published_year) if published_year else book["published_year"]
            except ValueError:
                print("Invalid input! Keeping the original year.")
                published_year = book["published_year"]

            genre = input(f"New genre (press Enter to keep '{book['genre']}'): ").strip() or book["genre"]
            read_status = input(f"New read status (read/unread, press Enter to keep '{book['read_status']}'): ").strip().lower() or book["read_status"]

            book.update({"title": title, "author": author, "published_year": published_year, "genre": genre, "read_status": read_status})
            print("Book updated successfully!")
            return library

    print("Book not found.")
    return library

def view_library_stats(library):
    total_books = len(library)
    read_books = len([book for book in library if book["read_status"]=="read"])
    unread_books = total_books - read_books

    print(f"\nLibrary Stats:")
    print(f"Total books: {total_books}")
    print(f"Books read: {read_books}")
    print(f"Books unread: {unread_books}")

def list_books(library):
    if not library:
        print("No books in the library yet.")
        return
    
    print("\nYour Library:")
    for book in library:
        print(f"ID: {book['id']} | Title: {book['title']} | Author: {book['author']} | Year: {book['published_year']} | Genre: {book['genre']} | Read: {book['read_status']}")

def search_book(library):
    search_id = int(input("Enter id to search: "))
    found_books = [book for book in library if search_id == book["id"]]

    if found_books:
        print("\nSearch Results:")
        for book in found_books:
            print(f"ID: {book['id']} | Title: {book['title']} | Author: {book['author']} | Year: {book['published_year']} | Genre: {book['genre']} | Read: {book['read_status']}")
    else:
        print("No books found.")

def main():
    library = []
    next_book_id = 1

    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            library, next_book_id = add_book(library, next_book_id)
        elif choice == "2":
            library = remove_book(library)
        elif choice == "3":
            library = update_book(library)
        elif choice == "4":
            view_library_stats(library)
        elif choice == "5":
            list_books(library)
        elif choice == "6":
            search_book(library)
        elif choice == "7":
            print("Exiting the Library Manager. Have a great day!")
            break
        else:
            print("Invalid choice. Please try again.")


main()