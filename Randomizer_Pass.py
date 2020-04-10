import random

pass_len = int(input())
password = ''
i = 0

zahl = '1234567890'
alpha = 'abcdefghijklmnopqrstuvwxyz'
big_alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
symbols = '!@#$%^&*()-+'

while i < pass_len:
    i += 1
    password += random.choice(zahl + alpha + big_alpha + symbols)
    print(password)

print(password)

