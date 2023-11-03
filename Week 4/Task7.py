import numpy
temps = ["23C","34C","21C","15C","31C","23C"]

for i in range(0,6):
    temps[i] = int(temps[i][:-1])
print(f"Mean is {numpy.mean(temps)}")
print(f"Max is {numpy.max(temps)}")
print(f"Min is {numpy.min(temps)}")