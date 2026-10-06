def read_float(prompt):
    """Считывает вещественное число с проверкой"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: введите число!")