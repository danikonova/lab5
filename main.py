#Задана рекуррентная функция.
# Область определения функции – натуральные числа.
# Написать программу сравнительного вычисления данной функции рекурсивно и итерационно.
# Определить границы применимости рекурсивного и итерационного подхода.
# Результаты сравнительного исследования времени вычисления представить в табличной и графической форме.
# вариант 21.	F(1) = 1, F(2) = 1, F(n) = F(n-2)*n + 2, при n > 2

import time
import matplotlib.pyplot as plt
# Рекурсивное вычисление функции
def recursive_f(n):
    if n == 1 or n == 2:
        return 1
    else:
        return recursive_f(n - 2) * n + 2

# Итерационное вычисление функции
def iterative_f(n):
    if n == 1 or n == 2:
        return 1
    else:
        a, b = 1, 1
        for i in range(3, n + 1):
            a, b = b, b * (i - 2) + 2
        return b

# Ввод
n = int(input("Введите n (натуральное число > 2): "))
k = int(input("Введите шаг изменения функции k: "))

# Списки для сохранения результатов вычисления
recursive_results = []
iterative_results = []
x_values = []

# Вычисление функции
for i in range(1, n + 1, k):
    recursive_start_time = time.time()
    r = recursive_f(i)
    recursive_end_time = time.time()
    recursive_time = round(recursive_end_time - recursive_start_time, 7)

    iterative_start_time = time.time()
    it = iterative_f(i)
    iterative_end_time = time.time()
    iterative_time = round(iterative_end_time - iterative_start_time, 7)

    recursive_results.append(recursive_time)
    iterative_results.append(iterative_time)
    x_values.append(i)

# Вывод результатов
#print('| n | Recursive | Iterative |')
print("n\t Recursive time\tIterative time")
for i in range(len(x_values)):
    print("{0:>5}\t{1:<12.9f}\t{2:<10.7f}".format(x_values[i], recursive_results[i], iterative_results[i]))


plt.plot(x_values, recursive_results, label="Recursive")
plt.plot(x_values, iterative_results, label="Iterative")
plt.xlabel("n")
plt.ylabel("Time (seconds)")
plt.legend()
plt.show()
print("Как видно из таблицы и графика, время выполнения рекурсивного подхода быстро растет"
    "\nс увеличением n быстро становится непрактичным. Рекурсивный подход перестает работать при n равном 999 и больше."
      "\nИтерационный подход работает достаточно быстро и может вычислять значения для любых n.")

