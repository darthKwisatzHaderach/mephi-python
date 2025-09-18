# Задание №1. Замена символов в строках списка
# Условие задачи
# Дан список строк и два символа: старый и новый. Требуется написать функцию replace_characters(lst, old, new), которая заменяет все вхождения старого символа на новый в каждой строке списка.
# Входные данные:
#     lst: список строк
#     old: старый символ
#     new: новый символ
# Выходные данные:
#     - список строк с замененными символами
# Примеры использования:
#     replace_characters(["hello", "world"], "o", "1")               # ["hell1", "w1rld"]
#     replace_characters(["apple", "banana", "cherry"], "a", "o")    # ["opple", "bonono", "cherry"]
#     replace_characters(["abracadabra"], "a", "o")                  # ["obrocodobro"]
# Исключения и особые случаи:
#     Если в строке нет символа old — строка остаётся без изменений
#     Если lst — пустой список ([]), функция возвращает []
#     Символы old и new могут быть любыми, включая знаки препинания, пробелы и цифры
#     Заменяются все вхождения, не только первое
# Ограничения:
# Не использовать:
#     - filter()
#     - lambda
#     - списковые включения (list comprehension)

def replace_characters(lst, old, new):
    if not isinstance(lst, list):
        raise TypeError("lst must be a list of strings")
    if not isinstance(old, str) or not isinstance(new, str) or len(old) != 1 or len(new) != 1:
        raise TypeError("old and new must be single characters and str")

    result = []
    for item in lst:
        if not isinstance(item, str):
            raise TypeError("All elements in lst must be strings")
        result.append(item.replace(old, new))

    return result

# Пример использования
test_list = ["hello", "world"]
old_char = "o"
new_char = "1"

result = replace_characters(test_list, old_char, new_char)
print("Результат:", result)
