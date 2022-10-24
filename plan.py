array = list(map(int, input().split())) # пользольватель вводит массив целых чисел

# Вероятность найти ключ в i−м элементе Pi = 1/N
# Матожидание числа поисков E = N/2
# Число операций сравнений в худшем случае 2N.
# T(N) = 2 · N = O(N)
def dummysearch(a, key):
    N = len(a)
    for i in range(N):
        if a[i] == key:
            return i
    return N

def cleversearch(a, key):
    N = len(a)
    a[N] = key
    i = 0
    while a[i] != key:
        i += 1
    return i

# Число операций сравнения N в худшем случае.
# T(N) = N = O(N)
# Поиск ускорен в два раза!