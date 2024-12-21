def bubble_sort(arr):
    """
    Bubble Sort implementation that yields each step.
    :param arr: List of numbers to sort.
    :return: Generator yielding the array at each step.
    """
    arr = arr[:]
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            yield arr  # Yield the array state at each step

def selection_sort(arr):
    """
    Selection Sort implementation that yields each step.
    :param arr: List of numbers to sort.
    :return: Generator yielding the array at each step.
    """
    arr = arr[:]
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        yield arr  # Yield the array state at each step

def insertion_sort(arr):
    """
    Insertion Sort implementation that yields each step.
    :param arr: List of numbers to sort.
    :return: Generator yielding the array at each step.
    """
    arr = arr[:]
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        yield arr  # Yield the array state at each step
