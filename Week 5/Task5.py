import numpy
import sys

temps = []
if(len(sys.argv[1:]) != 0):
    for i in sys.argv[1:]:
        if (len(i)) == 0:
            break
        temps.append(i + "C")

    for i in range(0, len(temps)):
        temps[i] = int(temps[i][:-1])
    print(f"Mean is {numpy.mean(temps)}")
    print(f"Max is {numpy.max(temps)}")
    print(f"Min is {numpy.min(temps)}")
else:
    print("No values provided..")