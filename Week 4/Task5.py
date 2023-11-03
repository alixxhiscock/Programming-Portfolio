def FahrToCels(val):
    return (val-32)*5/9

def CelsToFarh(val):
    return (val * 9/5) + 32

print(FahrToCels(73.4))
print(CelsToFarh(23))