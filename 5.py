months = int(input("Введите количество месяцев: "))
years = int(input("Введите количество лет: "))


total_days = months * 29 + years * 12 * 29
total_hours = total_days * 24


print(f"Общее количество часов: {total_hours} часов")