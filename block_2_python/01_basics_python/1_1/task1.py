ishodnoe = input('Введите числа через пробел: ')
elements = ishodnoe.split()
numbers = []

for i in elements:
    number = float(i)
    numbers.append(number)

min_num = min(numbers)
max_num = max(numbers)
diff_num = max_num - min_num

print('Минимальное: ', min_num)
print('Максимальное: ',max_num)
print('Разница: ',diff_num)