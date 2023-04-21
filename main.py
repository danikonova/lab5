#Задана рекуррентная функция.
# Область определения функции – натуральные числа.
# Написать программу сравнительного вычисления данной функции рекурсивно и итерационно.
# Определить границы применимости рекурсивного и итерационного подхода.
# Результаты сравнительного исследования времени вычисления представить в табличной и графической форме.
# вариант 21.	F(1) = 1, F(2) = 1, F(n) = F(n-2)*n + 2, при n > 2

import time
import matplotlib.pyplot as plt


def recursive_f(n):
    if n == 1 or n == 2:
        return 1
    else:
        return recursive_f(n-2) * n + 2

def iterative_f(n):
    if n == 1 or n == 2:
        return 1
    else:
        f1 = 1
        f2 = 1
        fn = 0
        for i in range(3, n+1):
            fn = f1 * i + 2
            f1 = f2
            f2 = fn
        return fn


n = int(input("Введите n: "))
k = int(input("Введите шаг изменения функции: "))

print("n | Рекурсивное время | Итерационное время | Рекурсия | Итерация")
print("-" * 62)

for i in range(1, n+1, k):
    start_time = time.time()
    rec = recursive_f(i)
    end_time = time.time()
    rec_time = end_time - start_time

    start_time = time.time()
    it = iterative_f(i)
    end_time = time.time()
    it_time = end_time - start_time

    print("{:2d} | {:15f} | {:19f} | {:8d} | {:8d}".format(i, rec_time, it_time, rec, it))


n_list = range(1, n+1, k)
rec_time_list = []
it_time_list = []

for i in n_list:
    start_time = time.time()
    recursive_f(i)
    end_time = time.time()
    rec_time_list.append(end_time - start_time)

    start_time = time.time()
    iterative_f(i)
    end_time = time.time()
    it_time_list.append(end_time - start_time)

plt.plot(n_list, rec_time_list, label="Рекурсия")
plt.plot(n_list, it_time_list, label="Итерация")
plt.legend()
plt.show()