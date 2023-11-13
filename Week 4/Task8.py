import numpy
temps = []
inputvalue = "    "
while inputvalue:
    inputvalue = str(input("Enter temperature: "))
    if len(inputvalue) ==0:
        break
    temps.append(inputvalue+"C")
    print(temps)

for i in range(0,len(temps)):
    temps[i] = int(temps[i][:-1])
print(f"Mean is {numpy.mean(temps)}")
print(f"Max is {numpy.max(temps)}")
print(f"Min is {numpy.min(temps)}")