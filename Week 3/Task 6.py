valid = False
num = int(input("Enter Number:"))
while not valid:
    if 0<=num<=12:
        valid = True
        break
    else:
        print("Invalid Number (0-12)")
    num = int(input("Enter Number:"))

for i in range(0,num+1):
    print(f"{i} x 7 = {i*7}")