import hashlib
import os

#Sign-Up Fuction Start Here
def signup():
    email= input("Enter username: ")

    if os.path.exists("credentials.txt") and os.stat("credentials.txt").st_size>0:      #Check if the file exist
        with open("credentials.txt", "r") as f: #open File credentials.txt
            lines= f.read().splitlines()    #read lines on the file

#check if email already exist or not.
        for i in range (0, len(lines), 2): 
            stored_email = lines[i].strip()  
            if email == stored_email:
                print("Username already exist!")
                return #To exit the fuction if true
    pwd = input("Enter Password: ")
    conf_pwd = input("Comfirm Password ")

 #If both pass entered are the same, this will Hash the Password using SHA256
    if conf_pwd == pwd:
        #Hash the Password using SHA256
        enc = conf_pwd.encode()
        hash1 = hashlib.sha256(enc).hexdigest()
        
        with open("credentials.txt", "a") as f:   # Open credentials.txt file and append to this.
            f.write(email + "\n")           #append the email
            f.write(hash1 + "\n")           #append the password hash
        print("You have registered Successfully!")
    else: 
        print("Password Dont Match")
#Sign-Up Fuction END Here

#Log-In Fuction Start Here
def login():
    email = input("Enter Username: ")
    pwd= input("Enter Password: ")
    auth = pwd.encode()
    auth_hash= hashlib.sha256(auth).hexdigest() #Hash password entered to login

#Split Username from pass
    try:
        with open("credentials.txt", "r") as f: #Split Username from pass
            lines= f.read().splitlines()

        for i in range (0, len(lines), 2):
            if i+1<len(lines):
                stored_email = lines[i].strip()
                stored_pwd = lines[i+1].strip()

#Compare both User and Pass to make sure is correct. 
                if email == stored_email and auth_hash == stored_pwd:  
                    print("Authenticating........\n")
                    print("Logged in!")
                    return
        print("Wrong, !")

    except FileNotFoundError:
        print("Something went wrong")
## END login

#This is a menu, were we call both fuctions and interact with the code.
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
