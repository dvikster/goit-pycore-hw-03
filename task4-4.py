from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    # Отримуємо поточну дату
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        # Конвертуємо день народження у формат datetime.date
        birthday_date = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        # перевіряємо чи день народження в цьому році
        birthday_this_year = birthday_date.replace(year=today.year)
        
        # Якщо день народження вже був у цьому році, встановлюємо на наступний рік
        if birthday_this_year < today:
            birthday_this_year = birthday_date.replace(year=today.year + 1)
        
        # Визначаємо кількість днів до дня народження
        days_until_birthday = (birthday_this_year - today).days

        # Перевіряємо, чи день народження відбувається протягом наступних 7 днів
        if 0 <= days_until_birthday <= 7:
            # Якщо день народження припадає на вихідний (субота або неділя)
            if birthday_this_year.weekday() in (5, 6):
                # Переносимо на наступний понеділок
                congratulation_date = birthday_this_year + timedelta(days=(7 - birthday_this_year.weekday()))
            else:
                congratulation_date = birthday_this_year
            
            # Додаємо результат у список
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays

# Приклад використання
users = [
    {"name": "John Doe", "birthday": "1985.11.03"},
    {"name": "Jane Smith", "birthday": "1990.11.01"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
