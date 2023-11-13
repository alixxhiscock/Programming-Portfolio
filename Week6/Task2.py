def factors(val):
    factorslist = []
    for i in range(1,val+1):
        if val % i == 0:
            factorslist.append(i)
    return(factorslist)
print(factors(234))