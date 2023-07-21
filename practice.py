sequence = input("Введите последовательность чисел через пробел: ")
num = input("Введите любое число: ")


# Формируем список, где отсутствуют все не числовые значения
elements_list = []
for e in sequence.split():
    if e.isdigit():
        elements_list.append(int(e))


# Функция для сортировки
def function_sort(elements_list):
    for i in range(len(elements_list)):
        for j in range(len(elements_list) - i - 1):
            if elements_list[j] > elements_list[j + 1]:
                elements_list[j], elements_list[j + 1] = elements_list[j + 1], elements_list[j]
    return elements_list

# Поиск индекса заанного числа
def binary_search(sequence, num):
    low = 0
    high = len(sequence) - 1
    while low <= high:
        mid = (low + high) // 2
        if sequence[mid] == num:
            return mid
        elif sequence[mid] < num:
            low = mid + 1
        else:
            high = mid - 1
    return low


res_sort = function_sort(elements_list)
print(f'Список чисел по возрастанию:  {res_sort}')
print(f'Индекс введенного числа в заданной последовательности: ', binary_search(res_sort, num))