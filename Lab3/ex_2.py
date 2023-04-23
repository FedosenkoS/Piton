# Реализуйте рекурсивную функцию нарезания прямоугольника с заданными пользователем сторонами a и b
# на квадраты с наибольшей возможной на каждом этапе стороной.
# Выведите длины ребер получаемых квадратов и кол-во полученных квадратов.


a = int(input("Введите значение стороны А: "))
b = int(input("Введите значение стороны В: "))

def CutIntoSquares(a, b, count):
    while a!=0 and b!=0:
        if a > b:
            count += 1
            print(f"Квадрат № {count}, сторона квадрата: {b}")
            return CutIntoSquares(a - b, b, count)
        else:
            count += 1
            print(f"Квадрат № {count}, сторона квадрата: {a}")
            return CutIntoSquares(a, b - a, count)




if a>0 and b>0:
    CutIntoSquares(a, b, 0)
else:
    print("Введенные значения не могут быть сторонами прямоугольника")