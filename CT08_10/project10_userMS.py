import random

user_db = {"bob" : "1234567890abc"}
attempts_db = {"bob" : 0}
role_db = {"bob" : "admin"}

def generate_password(length):
    password = []
    for _ in range(length):
        password.append(chr(random.randint(33, 126)))
    return "".join(password)

def create_new_user(user_db, role_db):
    username = input("What is your username? ")
    while True:
        length = input("What is the length of your password? ")
        if not length.isnumeric():
            print("Please enter a number.")
        elif int(length) < 12:
            print("Your password must have at least 12 characters.")
        else:
            break
    while True:
        role = input("Enter your role: ").strip().lower()
        if role not in ["admin", "user"]:
            print('Please only type "admin" or "user".')
        else:
            break
    user_db[username] = generate_password(int(length))
    role_db[username] = role

    return user_db, role_db

def update_password(user_db):
    while True:
        user = input("What is your username? ")
        if user not in user_db:
            print("That user is not in our database.")
        else:
            break
    while True:
        password = input("Enter your current password: ")
        if password != user_db[user]:
            print("Password incorrect. Please try again.")
        else:
            break
    while True:
        length = input("What is the length of your new password? ")
        if not length.isnumeric():
            print("Please enter a number.")
        elif int(length) < 12:
            print("Your password must have at least 12 characters.")
        else:
            break
    user_db[user] = generate_password(int(length))
    return user_db
    
def login(user_db, attempts_db):
    auth_status = False
    user = input("Enter your username: ")
    if user in user_db:
        pw = input("Enter your password: ")
        if user_db[user] == pw and attempts_db[user] < 3:
            auth_status = True
        else:
            attempts_db[user] += 1
            print("Access denied.")
            if attempts_db[user] >= 3:
                print("Account locked.")
    else:
        print("User not found")

    if auth_status:
        attempts_db[user] = 0
    return auth_status

def view_user_data(user_db, role_db, user):
    if role_db[user] == "admin":
        for username in user_db:
            print(f"Username: {username}, Password: {user_db[username]}")
    else:
        print("Only admins can view user data.")

while True:
    action = input("a. Create a new user\nb. Update a password\nc. Login\nd. View user data\ne. Exit program\nYour command: ").strip().lower()
    if action not in ["a", "b", "c", "d", "e"]:
        print('Please only type "a", "b", "c", "d", or "e".')
    elif action == "a":
        create_new_user(user_db, role_db)
    elif action == "b":
        update_password(user_db)
    elif action == "c":
        login(user_db, attempts_db)
    elif action == "d":
        while True:
            user = input("Enter your username: ")
            if user not in user_db:
                print("That user is not in our database.")
            else:
                break
        view_user_data(user_db, role_db, user)
    else:
        print("Exiting program...")
        break