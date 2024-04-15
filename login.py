import time

def login():
    attempts = 0
    max_attempts = 3
    authenticated = False

    while attempts < max_attempts:
        username = input("\nEnter your username: ")
        password = input("Enter your password: ")

        if (username == 'ray') and (password == 'pwd'):
            authenticated = True
            break
        else:
            print("Wrong username or password, try again.\n")
            attempts += 1

    if authenticated:
        print("Welcome " + username + "!,login successful!")

    else:
        print("Max attempts reached,Access denied.")
        for i in range(1, 5):
                time.sleep(1)
                print('time wait ', i)
        while True:
            retry_choice = input("Would you like to retry? (y/n): ")
            if retry_choice.lower() == 'y':
                login()  # Call the login function again
                break
            elif retry_choice.lower() == 'n':
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Please enter 'y' to retry or 'n' to exit.")

login()
