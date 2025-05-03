try:
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    result = num1 / num2
    print(f"Результат деления: {result}")
except ZeroDivisionError:
    print("Ошибка: деление на ноль!")
except ValueError:
    print("Ошибка: введите числа корректно!")