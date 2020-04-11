import random
import re

list_of_lines = []
list_of_names = []
list_for_gen = []
true_lines = ''
wrong_lines = ''
pass_len = 12
check = ''

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

task_file = open('task_file.txt', 'r')

for line in task_file:
    list_of_lines = [line.split(', ')]
    for el in list_of_lines:
        if re.findall(r'\D+', el[1]) and re.findall(r'\D+', el[2]) and len(el[3]) == 7 and re.findall(r'\D+', el[4]):
            list_of_names.append(el[1])
            list_of_names.append(el[2])
            list_for_gen.append(list_of_names)
            w = email_gen(list_for_gen)
            list_of_names = []
            list_for_gen = []
            true_lines = true_lines + w[0] + line[:-1] + ', ' + pas_gen(pass_len) + '\n'
        else:
            wrong_lines = wrong_lines + line
task_file.close()

wrong_file = open('wrong_file.txt', 'w')
wrong_file.write(wrong_lines)
wrong_file.close()

task_file = open('task_file.txt', 'w')
task_file.write('EMAIL, NAME, LAST_NAME, TEL, CITY, PASSWORD\n' + true_lines)
task_file.close()