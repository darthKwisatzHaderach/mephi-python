# Задание №2. Трибоначчи
# Условие задачи
# Числа Трибоначчи — это обобщение чисел Фибоначчи, где каждое число является суммой трёх предыдущих.
# Последовательность начинается с:
#   T(0) = 0
#   T(1) = 1
#   T(2) = 1
#   T(n) = T(n-1) + T(n-2) + T(n-3), при n ≥ 3
# Напишите функцию tribonacci(n), которая возвращает n-е число Трибоначчи.
# Входные данные:
#   - n: целое неотрицательное число (int)
# Выходные данные:
#   - n-е число Трибоначчи: целое неотрицательное число (int)
# Примеры использования:
#   - tribonacci(4) → 2 (T(3)=2, так как 1+1+0=2)
#   - tribonacci(0) → 0
#   - tribonacci(1) → 1
#   - tribonacci(2) → 1
#   - tribonacci(10) → 149
#   - tribonacci(28) → 8646064
# Исключения и особые случаи:
#   - Если n не является целым числом, выбрасывается TypeError: "Input must be an integer."
#   - Если n < 0, выбрасывается ValueError: "Input must be a non-negative integer."
# Ограничения:
#   - n ≥ 0
# Требования к реализации:
#   - Использование минимального объёма памяти
#   - Проверка корректности входных данных (int, n ≥ 0)
#   - Запрещается использовать внешние библиотеки

def tribonacci(n):
    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")

    if n < 0:
        raise ValueError("Input must be a non-negative integer.")

    t: list[int] = [0, 1, 1]

    for i in range(3, n + 1):
        t.append(t[i - 1] + t[i - 2] + t[i - 3])

    return t[n]


# Пример использования
n = int(input("Введите номер числа Трибоначчи: "))
result = tribonacci(n)
print(f"T({n}) = {result}")
