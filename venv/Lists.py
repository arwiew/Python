list = [9, 4, 5, 2, 3]
newList = []
for i in list:
    if (i % 2) != 0:
       newList.append(i)
    else: continue
print(newList)

list = [5, 1, 3, 6, 1]
newList = []
check = list[0]
for i in list:
    if i > check:
       print(i, check)
       newList.append(i)
       check = i
    else:
       check = i
       continue
print(newList)

list = [5, 1, 3, 6, 1]
list.sort()
print(list)


