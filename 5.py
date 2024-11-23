def calculate_happiness(number):
    """
    Рекурсивна функція, яка обчислює щасливість дня
    (зводить число до однозначного).
    """
    while len(str(number)) > 1:
        number = sum(int(digit) for digit in str(number))
    return number

# Читаємо дату з файлу input.txt
with open('for_5.txt', 'r') as input_file:
    date_string = input_file.read().strip()  # Наприклад, "20231116"

# Перетворюємо дату на число
if date_string.isdigit():
    happiness = calculate_happiness(int(date_string))

    # Записуємо щасливість у файл output.txt
    with open('for_5.txt', 'w') as output_file:
        output_file.write(str(happiness))
        print("Щасливість дати:", happiness)
else:
    print("Помилка: у файлі for_5.txt знайдено некоректні дані.")
