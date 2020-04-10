#создание email и запись в файл

file = open('task_file.txt', 'r+')

list_of_lines = []
list_of_names = []
list = []
str = ''

def email_gen(list):
    emails = []
    for i in list:
        letter = 1
        while i[1] + '.' + i[0][0:letter] + '@company.io' in emails:
            letter += 1
        emails.append(i[1] + '.' + i[0][0:letter] + '@company.io')
    return emails

for line in file:
    list_of_lines = [line.split(', ')]
    for el in list_of_lines:
        el[4] = el[4][:-1].lower()
        if el[1].isalpha() and el[2].isalpha() and len(el[3]) == 7 and el[4].islower():
            list_of_names.append(el[1])
            list_of_names.append(el[2])
            list.append(list_of_names)
            w = email_gen(list)
            list_of_names = []
            list = []
            str = str + w[0] + line
        else: break

file.truncate(0)
file.write('\n' + str)
file.close()







