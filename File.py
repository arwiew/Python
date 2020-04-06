file = open('task_file.txt', 'r+')
# EMAIL, NAME, LAST_NAME, TEL, CITY

exit_list = []

list = []

str = ''

def email_gen(list):
    emails = []
    for i in list:
        letter = 1
        while i[1] + '.' + i[0][0:letter] + '@company.io' in emails:
            letter+=1
        emails.append(i[1] + '.' + i[0][0:letter] + '@company.io')
    return emails

list_of_names = []
for line in file:
    exit_list = [line.split(', ')]
    for el in exit_list:
        el[4] = el[4][:-1].lower()
        if el[1].isalpha() and el[2].isalpha() and len(el[3]) == 7 and el[4].islower():
            list_of_names.append(el[1])
            list_of_names.append(el[2])
            list.append(list_of_names)
            w = email_gen(list)
            list_of_names = []
            #print(w)
            #print(line)
            list = []
            str = str + w[0] + line + '\n'
        else: break

file.write(str)

print(str)
for line in file:
    print(line)





