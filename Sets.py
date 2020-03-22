set = {1, 2, 3, 4, 5, 6, 7, 8}
print(len(set))

set = {1, 2, 3, 4}
set2 = {1, 4, 5, 3}
check_list = set.intersection(set2)
check = []
for i in check_list:
    check.append(i)
print(len(check))


set = {1, 2, 3, 4}
set2 = {1, 4, 3}
check = set.intersection(set2)
check_len = len(set2)
check = []
for i in check_list:
    check.append(i)
print(len(check))
if check_len == len(check):
    print('set2 является подмножеством')
else:
    print('set 2 не является подмножеством')
