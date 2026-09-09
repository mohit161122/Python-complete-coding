username = input("Enter the username :")
password = input("Enter the password :")

if(username == "admin" and password == "pass"):
    print("Login Success")
else:
    if(username != "admin"):
        print("Wrong username")
    else:
        print("Wrong password")
