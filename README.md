📚 Library Management System
A Python-based Library Management System built as a student project to practice real-world programming concepts such as Object-Oriented Programming, file handling, CRUD operations, authentication, logging, and Git/GitHub workflow.
This project started as a simple library program and was gradually developed into a more complete command-line management system.

🚀 Features
🔐 User Authentication
➕ Add Books
👀 View All Books
🔎 Search Books
Search by Book ID
Search by Title
✏️ Update Book Details
🗑️ Delete Books
📖 Issue Books
🔄 Return Books
📊 Library Statistics
📄 Export Books to CSV
💾 JSON-based Data Storage
📝 Activity Logging
✅ Input Validation
🖥️ Command-Line Interface
🛠️ Technologies Used
Technology	Purpose
Python	Main programming language
OOP	Book model and program structure
JSON	Persistent book storage
CSV	Data export
Logging	Tracking system activities
Git	Version control
GitHub	Repository and project management
📂 Project Structure
library-management-system/
│
├── main.py
├── book.py
├── database.py
├── auth.py
├── logger.py
├── books.json
├── books.csv
├── logs/
├── .gitignore
├── requirments.txt
└── README.md
File Overview
main.py
Contains the main menu and connects all library operations.
book.py
Contains the Book class and book-related methods.

database.py
Handles saving/loading books using JSON and exporting data to CSV.

auth.py
Handles user login/authentication.

logger.py
Handles application activity logs.

books.json
Stores the library's book data.

books.csv
Contains exported book records.

⚙️ How to Run
1. Clone the repository
git clone https://github.com/Fuzailax-web/library-management-system-python.git
2. Open the project
cd library-management-system-python
3. Create a virtual environment
python3 -m venv venv
4. Activate it
macOS/Linux:
source venv/bin/activate
Windows:
venv\Scripts\activate
5. Run the program
python main.py
🧭 Main Menu
========== Library Management System ==========

1. Add Book
2. View Books
3. Search Book
4. Update Book
5. Delete Book
6. Issue Book
7. Return Book
8. Statistics
9. Export to CSV
10. Exit
🧠 Concepts Practiced
This project helped me understand how individual Python concepts work together in an actual application.
Object-Oriented Programming
Created a Book class to represent individual books.
book = Book(book_id, title, author, category, year)
Each book is treated as an object containing its own data and status.
CRUD Operations
Implemented the four fundamental database-style operations:
Create → Add Book
Read   → View/Search Book
Update → Update Book
Delete → Delete Book
File Handling
Used files to make data persistent instead of losing everything when the program closes.
JSON
Book objects are converted into dictionaries and stored in books.json.
CSV
Library data can be exported into a spreadsheet-friendly books.csv file.
Exception Handling
Used try/except to prevent invalid input from crashing the program.
Logging
Important actions such as adding, updating, deleting, issuing, and returning books are recorded through the logging system.
Git & GitHub
Used Git throughout development to:
Track changes
Create meaningful commits
Push milestones
Maintain the project remotely
📊 Book Status System
Each book has a status:
Available
    ↓
  Issue
    ↓
 Issued
    ↓
 Return
    ↓
Available
This introduced the concept of state management in a simple real-world application.
🎯 What I Learned
Building this project helped me move beyond writing individual Python programs and understand how to structure a small application.
Some of the main things I practiced were:

Breaking a problem into multiple Python files
Creating and using classes
Working with objects and attributes
Managing lists of objects
Reading and writing JSON data
Exporting structured data to CSV
Validating user input
Handling exceptions
Maintaining application logs
Building a menu-driven application
Using Git and GitHub throughout development
Debugging errors instead of just rewriting the program
🔮 Future Improvements
Possible improvements for future versions:
🖥️ Graphical User Interface
🗄️ SQLite/MySQL database
👥 Multiple user roles
📅 Due dates and return deadlines
💰 Fine calculation
🔍 Better search and filtering
📈 Advanced statistics
🌐 Web-based version
🔑 Password hashing
📱 REST API
📌 Project Status
Version 1.0 — Completed ✅
The current version contains the core library management functionality and demonstrates the fundamental concepts I wanted to learn through the project.

👨‍💻 About the Project
This project was developed as part of my journey to improve my Python, programming, and software development skills.
Rather than trying to build a huge system immediately, I focused on building the project step-by-step, understanding each feature, debugging errors, and using Git to track the development process.

⭐ If You Find This Project Useful
Feel free to explore the code, suggest improvements, or use the project as a learning reference.
Built with Python 🐍 | Learning by Building 🚀

