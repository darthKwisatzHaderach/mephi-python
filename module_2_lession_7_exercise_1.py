# Задание №1. Вычисление экспоненциального роста
# Условие задачи
# Вы аналитик в стартапе, и вам нужно прогнозировать количество пользователей вашего продукта в следующие
# несколько месяцев, предполагая, что каждый месяц количество пользователей увеличивается на определенный процент.
# Вам нужно определить, через сколько месяцев количество пользователей превысит определенный порог.
# Напишите функцию calculate_months_to_threshold(start, rate, threshold) для реализации данного подхода, где:
#   start — количество пользователей в первый месяц (начальное значение)
#   rate — темп ежемесячного роста в процентах
#   threshold — значение, которое необходимо превысить
# Входные данные:
#   start: int
#   rate: int или float
#   threshold: int
# Выходные данные:
#   int: количество месяцев, необходимых, чтобы превысить threshold
# Примеры использования:
#   calculate_months_to_threshold(1000, 10, 2000) → 8
#   calculate_months_to_threshold(1797, 11, 9161) → 16
#   calculate_months_to_threshold(100, 50, 500) → 5
# Исключения и особые случаи:
#   - Если start >= threshold, результат должен быть 0 — цель уже достигнута
#   - Если rate <= 0, выбрасывается ValueError: "Growth rate must be greater than 0."
#   - Если start <= 0 или threshold <= 0, выбрасывается ValueError: "Start and threshold must be positive numbers."
# Ограничения:
#   - Все входные значения должны быть положительными числами
#   - rate может быть дробным (например, 2.5, 0.1), но не нулём и не отрицательным

def calculate_months_to_threshold(start, rate, threshold):
    if rate <= 0:
        raise ValueError("Growth rate must be greater than 0.")

    if start | threshold <= 0:
        raise ValueError("Start and threshold must be positive numbers.")

    if start >= threshold:
        return 0

    months = 0
    total = start
    monthly_rate = rate * 0.01

    while total < threshold:
        total += total * monthly_rate
        months += 1

        # Защита от бесконечного цикла
        if months > 1000:
            break

    return months

# Пример использования
start = int(input("Введите начальное количество пользователей: "))
rate = float(input("Введите темп роста в процентах: "))
threshold = int(input("Введите пороговое значение: "))

months = calculate_months_to_threshold(start, rate, threshold)
print(f"Количество месяцев для достижения порога: {months}")