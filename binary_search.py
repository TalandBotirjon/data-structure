


def binary_search(value, lists):
    low = 1
    high = len(lists) - 1
    step = 0
    while True:
        step += 1
        index = (low + high) // 2
        if value == lists[index]:
            return f"the {value} was found in {step} steps from the list"
        elif value > lists[index]:
            low = index
        elif value < lists[index]:
            high = index + 1
    return f"the {value} was not found in the {step} steps from the list"


lists = [12, 24, 35, 45, 56, 67, 78, 89, 99, 101]
print(binary_search(99, lists))

