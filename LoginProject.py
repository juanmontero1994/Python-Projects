import hashlib
import os

def signup():
    email= input("Enter username: ")

    if os.path.exists("credentials.txt") and os.stat("credentials.txt").st_size>0:
        with open("credentials.txt", "r") as f:
            lines= f.read().splitlines()

        for i in range (0, len(lines), 2):
            stored_email = lines[i].strip()
            if email == stored_email:
                print("Username already exist!")
                return #To exit the fuction if true
    pwd = input("Enter Password: ")
    conf_pwd = input("Comfirm Password ")

    if conf_pwd == pwd:
        #Hash the Password using SHA256
        enc = conf_pwd.encode()
        hash1 = hashlib.sha256(enc).hexdigest()
        
        with open("credentials.txt", "a") as f:
            f.write(email + "\n")
            f.write(hash1 + "\n")
        print("You have registered Successfully!")
    else: 
        print("Password Dont Match")

def login():
    email = input("Enter Username: ")
    pwd= input("Enter Password: ")
    auth = pwd.encode()
    auth_hash= hashlib.sha256(auth).hexdigest()

    try:
        with open("credentials.txt", "r") as f:
            lines= f.read().splitlines()

        for i in range (0, len(lines), 2):
            if i+1<len(lines):
                stored_email = lines[i].strip()
                stored_pwd = lines[i+1].strip()

                if email == stored_email and auth_hash == stored_pwd:
                    print("Authenticating........\n")
                    print("Logged in!")
                    return
        print("Wrong !")

    except FileNotFoundError:
        print("Something went wrong")
    
    ## END login

while True: 
    print("-------------- SignUp and Logging Up---------------")
    print("1. Sign-Up")
    print("2.Log-In")
    print("3.Close")

    try:
        ch = int(input("Select a Option: "))
        if ch==1:
            signup()
        elif ch==2:
            login()
        elif ch==3:
            print("Thanks for Using this service!")
            break
        else:
            print("Invalid Option")
    except ValueError:
        print("Invalid input! Please Select Options 1, 2 or 3")    
