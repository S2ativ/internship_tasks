import numpy as np

n, m = int(input("Введите n: ")), int(input("Введите m: "))
arr = np.random.randint(1, 101, size=(n, m))
summ = np.sum(arr, axis=1)

print("Сумма элементов в каждой строке: ", summ)
