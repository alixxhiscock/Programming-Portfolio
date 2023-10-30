valid = False
num = int(input("Enter Number:"))
while not valid:
    if -12<=num<=12:
        valid = True
        break
    else:
        print("Invalid Number (0-12)")
    num = int(input("Enter Number:"))

if(num < 0):
    for i in reversed(range(0,-(num - 1))):
        print(f"{i} x 7 = {i * 7}")
else:
    for i in range(0, num + 1):
        print(f"{i} x 7 = {i * 7}")