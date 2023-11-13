import random
def hidemsg(val):
    msg = ""
    interval = random.randint(2,20)
    for i in val:
        msg += i
        msg += ("x"*interval)
    return msg

print(hidemsg("test"))