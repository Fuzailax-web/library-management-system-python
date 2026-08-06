import json
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