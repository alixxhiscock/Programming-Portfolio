password = str(input("Enter password: "))
invalid = True
while invalid:
    if(len(password) >= 8 and len(password) <= 12):
        invalid = False
        break
    print("Must be between 8 and 12 characters long")
    password = str(input("Enter password: "))

if password == str(input("Enter password: ")):
    print("Password Set")
else:
    print("Invalid Password")