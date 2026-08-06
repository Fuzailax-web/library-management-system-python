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

def add_book():

    try:
        book_id = int(input("Enter Book ID: "))
    except ValueError:
        print("\n❌ Book ID must be a number!")
        return

    # Check duplicate Book ID
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

    try:
        quantity = int(input("Enter Quantity: "))
    except ValueError:
        print("\n❌ Quantity must be a number!")
        return

    if quantity <= 0:
        print("\n❌ Quantity must be greater than 0!")
        return

    book = Book(book_id, title, author, quantity)

    books.append(book)

    save_books(books)

    logger.info(f"Book Added: {book.title} (ID: {book.book_id})")

    print("\n✅ Book Added Successfully!")


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

    elif choice == "10":
         print("\nThank you for using Library Management System!")
         break

else:
    print("\n❌ Invalid Choice!")