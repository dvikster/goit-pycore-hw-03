from datetime import datetime

def get_days_from_today(date):
    # Перетворення рядка дати у форматі 'YYYY-MM-DD' на об'єкт datetime
    given_date = datetime.strptime(date, '%Y-%m-%d').date()
    # Отримання поточної дати
    today = datetime.today().date()
    # Обчислення різниці між поточною датою і заданою датою
    delta = today - given_date
    # Повернення різниці у днях
    return delta.days

# Приклади використання
print(get_days_from_today('2024-10-20'))  # Виведе кількість днів від '2020-10-09' до сьогодні
print(get_days_from_today('2024-11-10'))  # Виведе від'ємне значення для дати в майбутньому





