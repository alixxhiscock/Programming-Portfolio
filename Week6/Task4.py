def encrypt(val):
    return val.replace(" ","")[::-1]

print(encrypt("test word"))
