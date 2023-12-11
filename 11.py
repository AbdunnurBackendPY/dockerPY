import random


random_numbers = [random.randint(1, 100) for _ in range(20)]


even_count = sum(1 for num in random_numbers if num % 2 == 0)
odd_count = sum(1 for num in random_numbers if num % 2 != 0)


print(f"Четных чисел: {even_count}, Нечетных чисел: {odd_count}")