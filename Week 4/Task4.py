def removelast(param):
    if len(param) <=1:
        return param
    else:
        return param[:-1]

print(removelast("abcdef"))