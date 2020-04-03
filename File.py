file = open('task_file.txt', 'r+')
# EMAIL, NAME, LAST_NAME, TEL, CITY
#str = file.read()
#set = [str.split(',')]
#print(set)
exit_list = []
list_of_names = []
list = []
itog_list = []
check = 0

for line in file:
    exit_list = [line.split(', ')]
    for el in exit_list:
        list_of_names.append(el[1])
        list_of_names.append(el[2])
        break
    list.append(list_of_names)
    list_of_names = []

for elem in list:
    list.email_gen()

print(exit_list)
print(list_of_names)
print(list)
print(itog_list)








def email_gen(list_of_names):
    emails = []
    for i in list_of_names:
        letter = 1
        while i[1] + '.' + i[0][0:letter] + '@company.io' in emails:
            letter+=1
        emails.append(i[1] + '.' + i[0][0:letter] + '@company.io')
    return emails