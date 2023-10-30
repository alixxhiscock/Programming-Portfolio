password = str(input("Enter password: "))
invalid = 0
notbad = False
lengthcheck = False
bad_passwords = ['password','letmein','sesame','hello','justinbieber']
while not lengthcheck or not notbad:
    if 8 <= len(password) <= 12:
        lengthcheck = True
    else:
        print("Must be between 8 and 12 characters long.")
    if password not in bad_passwords:
        notbad = True
    else:
        print("Not a secure password.")
    if lengthcheck and notbad:
        break
    password = str(input("Enter password: "))

if password == str(input("Enter password: ")):
    print("Password Set")
else:
    print("Invalid Password")