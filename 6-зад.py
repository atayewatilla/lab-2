import re
from datetime import datetime

# Чтение файла
with open('text.txt', 'r') as file:
    text = file.read()

# Поиск дат
dates = re.findall(r'\b\d{2}\.\d{2}\.\d{4}\b', text)

# Преобразование формата
converted_dates = []
for date in dates:
    try:
        dt = datetime.strptime(date, '%d.%m.%Y')
        converted_dates.append(dt.strftime('%Y-%m-%d'))
    except ValueError:
        continue

# Сортировка дат
sorted_dates = sorted(converted_dates, key=lambda x: datetime.strptime(x, '%Y-%m-%d'))

# Сохранение
with open('dates.txt', 'w') as file:
    file.write('\n'.join(sorted_dates))

print("Отсортированные даты сохранены в dates.txt")