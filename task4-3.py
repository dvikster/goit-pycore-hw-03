import re

def normalize_phone(phone_number):
    # Видаляємо всі символи, крім цифр та '+' на початку
    clean_number = re.sub(r"[^\d+]", "", phone_number)

    # Якщо номер починається з '380', додаємо лише '+'
    if clean_number.startswith("380"):
        clean_number = "+" + clean_number
    # Якщо номер починається з '80', додаємо лише '+3' - перевірка, для людей, які досі пишуть номери починаючи з 8, таких мало, але вони все ще існують:)
    if clean_number.startswith("80"):
        clean_number = "+3" + clean_number
    # Якщо номер починається з '0', додаємо код країни '+38'
    elif clean_number.startswith("0"):
        clean_number = "+38" + clean_number

    return clean_number

# Приклад використання
raw_numbers = [
    "067\t123 4567",
    "(095) 234-5678\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
    " 8050 111 22 22 ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
