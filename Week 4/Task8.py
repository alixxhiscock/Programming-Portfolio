import numpy
temps = []
inputvalue = "    "
while inputvalue:
    if len(inputvalue) < 1:
        print(len(inputvalue))
        break
    print(inputvalue)
    inputvalue = str(input("Enter temperature: "))
    temps.append(inputvalue+"C")
    print(temps)

for i in range(0,len(temps)):
    temps[i] = int(temps[i][:-1])
print(f"Mean is {numpy.mean(temps)}")
print(f"Max is {numpy.max(temps)}")
print(f"Min is {numpy.min(temps)}")

# Not working for some reason as not catching null value
# Making it go into for loop where operation's can't be performed on null value
# Will try fix ASAP