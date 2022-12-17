def bubblesort(array: list, reverse=False) -> list:
    """
    List sorted function bubble sort.

    :param array: Sorted this array.
    :param reverse: Sorted growth reverse False. Sorted decrease reverse True.
    :return: Sorted and returned.
    """
    if reverse:
        for i in range(len(array)):
            for j in range(len(array)-1-i):
                if array[j] < array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]
        return array

    for i in range(len(array)):
        for j in range(len(array)-1-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array


array = [5, 2, 6, 0, 7, 1, 4, 9, 3]  # List elements not sorted.
print(bubblesort(array))  # List sorted growth.


print(bubblesort(array, reverse=True))  # List sorted decrease.

