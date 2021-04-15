""" Remove duplicated from the list:
a = [10,20,30,20,10,50,60,40,80,50,40] and store the values in the same list """

a = [10,20,30,20,10,50,60,40,80,50,40]
res = []
for x in a:
    if x not in res:
        res.append(x)
print(res)