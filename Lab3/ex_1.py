import random
import datetime
import prettytable  # пакет для таблицы
import matplotlib.pyplot as plt  # библиотека для графика


def BubbleSort(A):  # сортировка пузырьком
    for i in range(len(A)):
        for j in range(len(A) - 1 - i):
            if A[j] > A[j + 1]:
                a = A[j]
                A[j] = A[j + 1]
                A[j + 1] = a


def QuickSort(A, fst, lst):  # быстрая сортировка
    if fst >= lst:
        return

    # i, j = fst, lst
    pivot = A[fst]
    # pivot = A[random.randint(fst, lst)]
    first_bigger = fst + 1
    while first_bigger <= lst:
        if A[first_bigger] >= pivot:
            break
        first_bigger += 1
    i = first_bigger + 1
    while i <= lst:
        if A[i] < pivot:
            A[i], A[first_bigger] = A[first_bigger], A[i]
            first_bigger += 1
        i += 1

    last_smaller = first_bigger - 1
    A[fst], A[last_smaller] = A[last_smaller], A[fst]
    QuickSort(A, fst, last_smaller - 1)
    QuickSort(A, first_bigger, lst)


# Цикл 1 – по i от 0 до N-1 :		# i - счетчик прохода по списку
# 	Действие – объявление переменной m = i;	# m - номер для мин. из неотсортированных
# 	Цикл 2 – по j от i до N :		# j - счетчик позиции при проходе по неотсортированной части
# 		Условие если A[j]<A[m] :	 # сравнение текущего элемента с текущим минимальным
# 			Действие – запоминаем номер обнаруженного нового минимального эл-та m = j
# 	Действие – перестановка местами A[m] и A[i]

def SelectSort(A):  # сортировка select
    for i in range(len(A) - 1):
        m = i
        for j in range(i, len(A)):
            if A[j] < A[m]:
                m = j
        a = A[i]
        A[i] = A[m]
        A[m] = a


table = prettytable.PrettyTable(["Размер списка", "Время пузырька", "Время быстрой", "Время select"])
x = []
y1 = []
y2 = []
y3 = []

for N in range(1000, 5001, 1000):
    x.append(N)
    min = 1
    max = N
    A = []
    for i in range(N):
        A.append(int(round(random.random() * (max - min) + min)))

    #print(A)

    B = A.copy()
    C = A.copy()
    # print(B)

    #BubbleSort(A)
    print("---")
    # print(A)

    # QuickSort(B, 0, len(B)-1)
    print("---")
    # print(B)

    SelectSort(C)
    print("---")
    print(C)

    t1 = datetime.datetime.now()
    BubbleSort(A)
    t2 = datetime.datetime.now()
    y1.append((t2 - t1).total_seconds())
    print("Пузырьковая сортировка   " + str(N) + "   заняла   " + str((t2 - t1).total_seconds()) + "c")

    t3 = datetime.datetime.now()
    QuickSort(B, 0, len(B) - 1)
    t4 = datetime.datetime.now()
    y2.append((t4 - t3).total_seconds())
    print("Быстрая   " + str(N) + "   заняла   " + str((t4 - t3).total_seconds()) + "c")

    t5 = datetime.datetime.now()
    SelectSort(C)
    t6 = datetime.datetime.now()
    y3.append((t6 - t5).total_seconds())
    print("Sort   " + str(N) + "   заняла   " + str((t6 - t5).total_seconds()) + "c")

    table.add_row([str(N), str((t2 - t1).total_seconds()), str((t4 - t3).total_seconds()), str((t6 - t5).total_seconds())])
print(table)


plt.plot(x, y1, "C0")
plt.plot(x, y2, "C1")
plt.plot(x, y3, "C2")
plt.show()
