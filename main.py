from random import randint
import time

a, b = map(int, input("Введите диапозон чисел через пробел: ").split())
n = int(input("Введите размер массива: "))

start = time.time()

A = [randint(a, b) for i in range(n)]
SUM = sum(A)

end = time.time() - start

print("Созданный массив:\n", A)
print("Длина массива: ", len(A))
print(f"""Сумма всего массива: {SUM}""")
print("Затраченное время: ", round(float(end), 4))