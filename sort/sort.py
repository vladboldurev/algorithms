#coding=utf-8

def insert_sort(a):
    """ сортировка списка вставками"""
    n = len(a)

    for top in range(1, n):
        k = top
        while k > 0 and a[k] < a[k - 1]:
            a[k], a[k - 1] = a[k - 1], a[k]
            k -= 1


def choice_sort(a):
    """сортировка списка выбором"""
    n = len(a)
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]


def bubble_sort(a):
    """сортировка пузырьком"""
    n = len(a)

    for bypass in range(1, n):
        for k in range(0, n - bypass):
            if a[k] > a[k + 1]:
                a[k], a[k + 1] = a[k + 1], a[k]


def test_method_1(mass):
    """test 1"""
    n = len(mass)

    for k in range(1, n):
         while k > 0 and mass[k] < mass[k - 1]:
            mass[k], mass[k - 1] = mass[k - 1], mass[k]
            k -= 1



def test_method_2(mass):
    """test 2"""
    n = len(mass)

    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if mass[i] > mass[j]:
                mass[i], mass[j] = mass[j], mass[i]


def test_mehtod_3(mass):
    """test 3"""
    n = len(mass)

    for i in range(1, n):
        for j in range(0, n - i):
            if mass[j] > mass[j + 1]:
                mass[j], mass[j + 1] = mass[j + 1], mass[j]





def count_sort(a, max_value):
    """сортирвока подсчетом кол-ва"""
    f = [0] * max_value
    n = len(a)

    for i in range(n):
        f[a[i] - 1] += 1

    print('f', f)

    for i in range(0, max_value):
        a += [i + 1] * f[i]

    print('count_sort', a)


def test_sort(sort_method):
    print("тестируем: ", sort_method.__doc__)
    print("test case #1", end=" ")
    a = [4, 2, 5, 1, 3]
    print(a)
    a_sorted = [1, 2, 3, 4, 5]
    sort_method(a)
    print(a)
    print("OK" if a == a_sorted else "False")

    print("test case #2", end=" ")
    a = list(range(10, 20)) + list(range(0, 10))
    a_sorted = list(range(20))
    sort_method(a)
    print("OK" if a == a_sorted else "False")

    print("test case #3", end=" ")
    a = [4, 2, 4, 2, 1]
    a_sorted = [1, 2, 2, 4, 4]
    sort_method(a)
    print("OK" if a == a_sorted else "False")


def test_count_sort(sort_method):
    print("тестируем: ", sort_method.__doc__)
    print("test case #4", end=" ")
    a = [4, 2, 4, 5, 2, 1, 5, 7, 9, 8, 9, 2, 1, 3, 4, 6]
    # a_sorted = [1, 2, 2, 4, 4]
    sort_method(a, 9)
    # print("OK" if a == a_sorted else "False")

def bubble_sort_second(list_data):
    n = len(list_data)
    for j in range(1, n):
        for i in range(0, n - j):
            if list_data[i] > list_data[i + 1]:
                list_data[i], list_data[i + 1] = list_data[i + 1], list_data[i]

    return list

def bubble_sort_third(list_data):

    position = len(list_data) - 1
    exchanges = True

    while position > 0 and exchanges:
        exchanges = False
        for i in range(position):
            if list_data[i] > list_data[i + 1]:
                exchanges = True
                list_data[i], list_data[i + 1] = list_data[i + 1], list_data[i]

        position -= 1

def choice_sort(list_data):
    number = len(list_data)
    index_max_element = 0
    for i in range(number - 1, 0, -1):
        index_max_element = 0
        for j in range(1, i + 1):
            if list_data[j] > list_data[index_max_element]:
                index_max_element = j

        list_data[index_max_element], list_data[i] = list_data[i], list_data[index_max_element]



if __name__ == "__main__":
    test_sort(choice_sort)
    # test_sort(bubble_sort_third)
    # test_sort(test_method_2)
    # test_count_sort(count_sort)
