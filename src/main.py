import math

def solve_quadratic(a, b, c):
    """Решает уравнение ax^2 + bx + c = 0"""
    d = b**2 - 4*a*c
    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2*a)
        x2 = (-b - math.sqrt(d)) / (2*a)
        return x1, x2
    elif d == 0:
        return -b / (2*a)
    else:
        return None

if __name__ == "__main__":
    a = float(input("Введите a: "))
    b = float(input("Введите b: "))
    c = float(input("Введите c: "))
    print("Результат:", solve_quadratic(a, b, c))