def quick_sort(arr):
    """
    Сложность сортировки:
        средний случай: O(n*log n)
            список делится примерно поровну, уровней получается около log n,
            на каждом уровне просматривается примерно n чисел, итого n*log n
        худший случай: O(n^2)
            каждый раз выбирается один элемент,который делит список на два,в одном из которых 0 элементов,а в другом (n-1) элементов
            и каждый раз проходимся по списку,уменьшая кол-во операций на 1, в итоге получается (n*(n-1))/2 ~ n^2
    """
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]

        low = [i for i in arr[1:] if i <= pivot]
        high = [i for i in arr[1:] if i > pivot]

        return quick_sort(low) + [pivot] + quick_sort(high)


import random

rand_arr = [random.randint(1, 200) for i in range(60)]
print(rand_arr)
print(quick_sort(rand_arr))
