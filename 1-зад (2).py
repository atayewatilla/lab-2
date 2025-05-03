# Чтение чисел из файла
with open('data.txt', 'r') as file:
    numbers = [float(line.strip()) for line in file]

# Вычисление статистик
sum_num = sum(numbers)
average = sum_num / len(numbers)
max_num = max(numbers)
min_num = min(numbers)

# Сохранение результатов
with open('result.txt', 'w') as file:
    file.write(f"Сумма: {sum_num}\n")
    file.write(f"Среднее: {average}\n")
    file.write(f"Максимум: {max_num}\n")
    file.write(f"Минимум: {min_num}\n")

print("Результаты сохранены в result.txt")