from auth import login
from database import save_books, load_books
from book import Book
from logger import logger


if not login():
    print("Exiting Program...")
    exit()


books = load_books()


def view_books():
    if len(books) == 0:
        print("\n📚 No books available in the library.")
        return

    print("\n========== Library Books ==========")

    for book in books:
        book.display()


def search_book():
    print("\n========== Search Book ==========")
    print("1. Search by Book ID")
    print("2. Search by Title")

    search_choice = input("Enter your choice: ")

    if search_choice == "1":
        try:
            search_id = int(input("Enter Book ID to search: "))
        except ValueError:
            print("\n❌ Book ID must be a number!")
            return

        for book in books:
            if book.book_id == search_id:
                print("\n✅ Book Found!")
                book.display()
                return

        print("\n❌ Book Not Found!")

    elif search_choice == "2":
        search_title = input("Enter Book Title to search: ").strip()

        for book in books:
            if book.title.lower() == search_title.lower():
                print("\n✅ Book Found!")
                book.display()
                return

        print("\n❌ Book Not Found!")

    else:
        print("\n❌ Invalid Choice!")


def add_book():
    try:
        book_id = int(input("Enter Book ID: "))
    except ValueError:
        print("\n❌ Book ID must be a number!")
        return

    for book in books:
        if book.book_id == book_id:
            print("\n❌ Book ID already exists!")
            return

    title = input("Enter Book Title: ").strip()

    if title == "":
        print("\n❌ Title cannot be empty!")
        return

    author = input("Enter Author Name: ").strip()

    if author == "":
        print("\n❌ Author name cannot be empty!")
        return

    category = input("Enter Category: ").strip()

    if category == "":
        print("\n❌ Category cannot be empty!")
        return

    try:
        year = int(input("Enter Publication Year: "))
    except ValueError:
        print("\n❌ Year must be a number!")
        return

    book = Book(book_id, title, author, category, year)

    books.append(book)
    save_books(books)

    logger.info(
        f"Book Added: {book.title} (ID: {book.book_id})"
    )

    print("\n✅ Book Added Successfully!")


def update_book():
    try:
        update_id = int(input("Enter Book ID to update: "))
    except ValueError:
        print("\n❌ Book ID must be a number!")
        return

    for book in books:
        if book.book_id == update_id:

            print("\n========== Current Book Details ==========")
            book.display()

            title = input("Enter New Title: ").strip()

            if title == "":
                print("\n❌ Title cannot be empty!")
                return

            author = input("Enter New Author: ").strip()

            if author == "":
                print("\n❌ Author cannot be empty!")
                return

            category = input("Enter New Category: ").strip()

            if category == "":
                print("\n❌ Category cannot be empty!")
                return

            try:
                year = int(input("Enter New Publication Year: "))
            except ValueError:
                print("\n❌ Year must be a number!")
                return

            book.title = title
            book.author = author
            book.category = category
            book.year = year

            save_books(books)

            logger.info(
                f"Book Updated: {book.title} (ID: {book.book_id})"
            )

            print("\n✅ Book Updated Successfully!")
            return

    print("\n❌ Book Not Found!")


def delete_book():
    try:
        delete_id = int(input("Enter Book ID to delete: "))
    except ValueError:
        print("\n❌ Book ID must be a number!")
        return

    for book in books:
        if book.book_id == delete_id:

            print("\n========== Book to Delete ==========")
            book.display()

            confirm = input(
                "Are you sure you want to delete this book? (y/n): "
            ).lower()

            if confirm == "y":
                books.remove(book)
                save_books(books)

                logger.info(
                    f"Book Deleted: {book.title} (ID: {book.book_id})"
                )

                print("\n✅ Book Deleted Successfully!")
                return

            print("\n❌ Delete cancelled!")
            return

    print("\n❌ Book Not Found!")


while True:
    print("\n========== Library Management System ==========")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Update Book")
    print("5. Delete Book")
    print("6. Issue Book")
    print("7. Return Book")
    print("8. Statistics")
    print("9. Export to CSV")
    print("10. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_book()

    elif choice == "2":
        view_books()

    elif choice == "3":
        search_book()

    elif choice == "4":
        update_book()

    elif choice == "5":
        delete_book()

    elif choice == "10":
        print("\nThank you for using Library Management System!")
        break

    else:
        print("\n❌ Invalid Choice!")