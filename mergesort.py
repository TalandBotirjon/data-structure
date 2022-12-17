
def mergesort(arr: list) -> list:
    """
    Sort algorithm Merge Sort.

    :param arr: Sorted this arr.
    :return: Sorted and returned.
    """
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        mergesort(left)
        mergesort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr


list1 = [14, 53, 222, 75, 343, 23, 87, 4554, 33]
print(mergesort(list1))
