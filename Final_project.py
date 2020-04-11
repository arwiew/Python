import random
'''Вам нужно написать программу, которая будет читать файл из предыдущего упражнения, заниматься его чисткой, 
формировать почтовые адреса для сотрудников, генерировать пароли безопасности для входа в почту, 
заносить информацию в этот файл и перезаписывать его.'''

list_of_lines = []
list_of_names = []
list_for_gen = []
str = ''
pass_len = 12

def pas_gen(pass_len):
    password = ''
    i = 0
    zahl = '1234567890'
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    big_alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    symbols = '!@#$%^&*()-+'
    while i < pass_len:
        i += 1
        password += random.choice(zahl + alpha + big_alpha + symbols)
    return password

def email_gen(list):
    emails = []
    for i in list:
        letter = 1
        while i[1] + '.' + i[0][0:letter] + '@company.io' in emails:
            letter += 1
        emails.append(i[1] + '.' + i[0][0:letter] + '@company.io')
    return emails

file = open('task_file.txt', 'r')

for line in file:
    list_of_lines = [line.split(', ')]
    for el in list_of_lines:
        el[4] = el[4][:-1].lower()
        if el[1].isalpha() and el[2].isalpha() and len(el[3]) == 7 and el[4].islower():
            list_of_names.append(el[1])
            list_of_names.append(el[2])
            list_for_gen.append(list_of_names)
            w = email_gen(list_for_gen)
            list_of_names = []
            list_for_gen = []
            str = str + w[0] + line[:-1] + ', ' + pas_gen(12) + '\n'
            print(str)
        else: break
file.close()

file = open('task_file.txt', 'w')
file.write('EMAIL, NAME, LAST_NAME, TEL, CITY, PASSWORD\n' + str)
file.close()