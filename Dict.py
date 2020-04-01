dict = {'Hello' : 'Hi', 'Bye' : 'Goodbye', 'List' : 'Array'}

# Вывод значения по ключу
say = input()
print(dict.get(say))
# Вывод ключа по значению
for key, value in dict.items():
        if say == value:
            print(key)



list = ['abc', 'bcd', 'abc', 'abd', 'abd', 'dcd', 'abc']
list.sort()
exlist = []
check = ''
for k in list:
    if k != check:
        exlist.append(k)
        check = k
    else: None
print(exlist)
even_list = []
for i in exlist:
    even_list.append(list.count(i))
print(even_list)