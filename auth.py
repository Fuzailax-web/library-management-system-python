import getpass

USERNAME = "admin"
PASSWORD = "admin123"


def login():
    print("\n========== Library Login ==========")

    username = input("Enter Username: ")
    password = getpass.getpass("Enter Password: ")

    if username == USERNAME and password == PASSWORD:
        print("\n✅ Login Successful!")
        return True

    print("\n❌ Invalid Username or Password!")
    return False