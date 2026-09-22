import random
import string

password = ''

print('''
      Варианты пароля:
      1)буквы
      2)буквы+цифры
      3)буквы+цифры+спецсимволы   
''')
passtype = int(input('введите соответствующий индекс типа пароля: '))
cnt = int(input('введите длину пароля: '))

if passtype == 1:
    pull = string.ascii_letters
elif passtype == 2:
    pull = string.ascii_letters + string.digits
elif passtype == 3:
    pull = string.ascii_letters + string.digits + string.punctuation
else:
    print('Неверный формат,формат по умолчанию "1"')
    pull = string.ascii_letters

for i in range(cnt):
    password += random.choice(pull)

print(f'Generated password:  {password}')
