def casecount(mystring):
    upper = 0
    lower = 0
    for i in mystring:
        if i.isupper():
            upper +=1
        else:
            lower +=1
    return upper, lower

print(casecount("myStRiNg"))
