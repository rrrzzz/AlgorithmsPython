import random


def quick_sort(array_to_sort):
    if len(array_to_sort) < 2:
        return

    quick_sort_recursive(array_to_sort, 0, len(array_to_sort) - 1)


def quick_sort_recursive(array_to_sort, start, end):
    if start >= end:
        return

    pivot_index = partition(array_to_sort, start, end)
    quick_sort_recursive(array_to_sort, start, pivot_index - 1)
    quick_sort_recursive(array_to_sort, pivot_index + 1, end)


def partition(array_to_sort, start, end):
    pivot = random.randrange(start, end + 1)
    swap_values(array_to_sort, pivot, start)

    smaller_end = start + 1
    for i in range(smaller_end, end + 1):
        if array_to_sort[i] < array_to_sort[start]:
            swap_values(array_to_sort, smaller_end, i)
            smaller_end += 1

    swap_values(array_to_sort, smaller_end - 1, start)
    return smaller_end - 1


def swap_values(array, first, second):
    temp = array[first]
    array[first] = array[second]
    array[second] = temp
