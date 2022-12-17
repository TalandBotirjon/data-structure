
from random import randrange


def qsort(array: list, reverse=False):
    """
    :param array: Sorted this array.
    :param reverse: Sorted growth reverse False. Sorted decrease reverse True.
    :return: Sorted and returned.
    """
    if reverse:
        if len(array) < 2:
            return array
        pivot = array.pop(randrange(len(array)))
        low = [i for i in array if i > pivot]
        high = [i for i in array if i <= pivot]
        return qsort(low, reverse) + [pivot] + qsort(high, reverse)

    if len(array) < 2:
        return array
    pivot = array.pop(randrange(len(array)))
    low = [i for i in array if i <= pivot]
    high = [i for i in array if i > pivot]
    return qsort(low) + [pivot] + qsort(high)


list1 = [14, 53, 222, 75, 343, 23, 87, 4554, 33]  # list elements int and not sort.
list2 = ['orange', 'pear', 'cherry','apple', 'grape', 'mango', 'plum']  # list elements string and not sort.


# list3 = qsort(list1)  # Sorted growth of list1.
# print(list3)

# list3 = qsort(list2)  # Sorted growth of list2.
# print(list3)


# list3 = qsort(list1, reverse=True)  # Sorted decrease of list1.
# print(list3)

# list3 = qsort(list2, reverse=True)  # Sorted decrease of list2.
# print(list3)
