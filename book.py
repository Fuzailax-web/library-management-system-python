class Book:
    def __init__(self, book_id, title, author, category, year):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.category = category
        self.year = year
        self.status = "Available"

def display(self):
    print("\n========== Book Details ==========")
    print(f"Book ID   : {self.book_id}")
    print(f"Title     : {self.title}")
    print(f"Author    : {self.author}")
    print(f"Category  : {self.category}")
    print(f"Year      : {self.year}")
    print(f"Status    : {self.status}")
    print("==================================")

def to_dict(self):
    return {
        "book_id": self.book_id,
        "title": self.title,
        "author": self.author,
        "category": self.category,
        "year": self.year,
        "status": self.status
    }
@classmethod
def from_dict(cls, data):
    book = cls(
        data["book_id"],
        data["title"],
        data["author"],
        data["category"],
        data["year"]
    )

    book.status = data["status"]

    return book