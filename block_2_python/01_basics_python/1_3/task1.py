data = input('Введи числа:')
data = [int(x) for x in data.split()]
def numbers(dataa):
    filtered = [ int(x) for x in dataa if x>=0 ]
    return sorted(filtered, reverse=True)
result = numbers(data)
print(result)