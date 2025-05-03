import re

# Чтение файла
with open('text.txt', 'r') as file:
    text = file.read()

# Поиск email-адресов
emails = re.findall(r'\b[\w.-]+@[\w.-]+\.\w+\b', text)
with open('emails.txt', 'w') as file:
    file.write('\n'.join(emails))

# Поиск телефонов
phones = re.findall(r'\+7-\d{3}-\d{3}-\d{2}-\d{2}', text)
with open('phones.txt', 'w') as file:
    file.write('\n'.join(phones))

# Поиск слов с заглавной буквы
capital_words = re.findall(r'\b[A-Z][a-z]*\b', text)
with open('capital_words.txt', 'w') as file:
    file.write('\n'.join(capital_words))

print("Результаты сохранены в emails.txt, phones.txt и capital_words.txt")