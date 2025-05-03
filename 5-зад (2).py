numbers = list(range(1, 21))

# Фильтрация четных чисел
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Четные числа:", even_numbers)

# Увеличение каждого числа на 10
increased = list(map(lambda x: x + 10, numbers))
print("Числа +10:", increased)

# Сортировка по убыванию
sorted_desc = sorted(numbers, key=lambda x: -x)
print("По убыванию:", sorted_desc)