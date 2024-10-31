import random

def get_numbers_ticket(min_val, max_val, quantity):
    # Перевірка вхідних параметрів на відповідність обмеженням
    if min_val < 1 or max_val > 1000 or quantity > (max_val - min_val + 1):
        return []
    
    # Генерація унікального набору випадкових чисел
    numbers = random.sample(range(min_val, max_val + 1), quantity)
    
    # Сортування списку чисел перед поверненням
    return sorted(numbers)

# Приклади використання
print(get_numbers_ticket(1, 49, 6))  # Виведе набір з 6 унікальних чисел від 1 до 49
print(get_numbers_ticket(1, 36, 5))  # Виведе набір з 5 унікальних чисел від 1 до 36
print(get_numbers_ticket(1, 10, 15)) # Виведе пустий список, оскільки quantity перевищує можливу кількість унікальних чисел
