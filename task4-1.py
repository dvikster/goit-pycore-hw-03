from datetime import datetime

def get_days_from_today(date):
    try:
        # Перетворення рядка дати у форматі 'YYYY-MM-DD' на об'єкт datetime
        given_date = datetime.strptime(date, '%Y-%m-%d').date()
    except ValueError:
        return "Невірний формат дати. Використовуйте формат 'YYYY-MM-DD'."

    # Отримання поточної дати
    today = datetime.today().date()
    # Обчислення різниці між поточною датою і заданою датою
    delta = today - given_date
    # Повернення різниці у днях
    return delta.days

# Приклади використання
print(get_days_from_today('2024-10-20'))  # Виведе кількість днів від '2024-10-20' до сьогодні
print(get_days_from_today('2024-11-10'))  # Виведе від'ємне значення для дати в майбутньому
print(get_days_from_today('20-10-2024'))  # Виведе повідомлення про помилку
