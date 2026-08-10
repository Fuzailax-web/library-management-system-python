import json
import csv
from book import Book

def save_books(books):
    
    with open("books.json", "w") as file:
        json.dump(
            [book.to_dict() for book in books],
            file,
            indent=4
        )

def load_books():
    try:
        with open("books.json", "r") as file:
            data = json.load(file)
            return [Book.from_dict(book) for book in data]

    except (FileNotFoundError, json.JSONDecodeError):
        return []

def export_to_csv():
    books = load_books()

    if len(books) == 0:
        print("\n❌ No books available to export.")
        return

    with open("books.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            "Book ID",
            "Title",
            "Author",
            "Category",
            "Year",
            "Status"
        ])

        for book in books:
            writer.writerow([
                book.book_id,
                book.title,
                book.author,
                book.category,
                book.year,
                book.status
            ])

    print("\n✅ Books exported successfully to books.csv")