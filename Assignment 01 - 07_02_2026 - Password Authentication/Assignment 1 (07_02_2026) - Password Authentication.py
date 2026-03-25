import re
import hashlib

# Simple in-memory "database"
users = {}

# Password validation function
def is_valid_password(password):
    if len(password) < 8:
        return "Password must be at least 8 characters long"
    
    if not re.search(r"[A-Z]", password):
        return "Password must contain at least one uppercase letter"
    
    if not re.search(r"[a-z]", password):
        return "Password must contain at least one lowercase letter"
    
    if not re.search(r"[0-9]", password):
        return "Password must contain at least one digit"
    
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "Password must contain at least one special character"
    
    return "Valid"


# Hashing function
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


# Register user
def register():
    username = input("Enter username: ")
    
    if username in users:
        print("Username already exists!")
        return
    
    password = input("Enter password: ")
    
    validation = is_valid_password(password)
    if validation != "Valid":
        print("Error:", validation)
        return
    
    users[username] = hash_password(password)
    print("Registration successful!")


# Login user
def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    if username not in users:
        print("User not found!")
        return
    
    if users[username] == hash_password(password):
        print("Login successful!")
    else:
        print("Incorrect password!")


# Main menu
def main():
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()