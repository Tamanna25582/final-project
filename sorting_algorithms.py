import numpy as np
import matplotlib.pyplot as plt
from random import randint, shuffle

def bubble_sort(li, x, delay):
    n = len(li)
    number_of_operations = 1
    color = [(0.2, 0.4, 0.6, 0.6)] * n
    for i in range(n):
        for j in range(0, n-i-1):
            color[j], color[j+1] = 'red', 'red'
            plt.bar(x, li, color=color)
            plt.title(f"Number of operations: {number_of_operations}")
            number_of_operations += 1
            plt.pause(delay)
            plt.clf()
            color[j], color[j+1] = (0.2, 0.4, 0.6, 0.6), (0.2, 0.4, 0.6, 0.6)
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
    plt.bar(x, li, color=color)
    plt.title(f"Number of operations: {number_of_operations}")
    plt.show()
            
    return li

def insertion_sort(li, x, delay):
    n = len(li)
    number_of_operations = 1
    color = [(0.2, 0.4, 0.6, 0.6)] * n
    for i in range(1, n):
        key_item = li[i]
        j = i - 1
        while j >= 0 and li[j] > key_item:
            color[j+1] = 'red'
            plt.bar(x, li, color=color)
            plt.title(f"Number of operations: {number_of_operations}")
            number_of_operations += 1
            plt.pause(delay)
            plt.clf()
            li[j + 1] = li[j]
            color[j+1] = (0.2, 0.4, 0.6, 0.6)
            j -= 1

        li[j + 1] = key_item

    plt.bar(x, li, color=color)
    plt.title(f"Number of operations: {number_of_operations}")
    plt.show()

    return li

def quicksort(li, x, delay, number_of_operations=0, type=""):
    n = len(li)
    X = np.arange(0, n, 1)

    if n < 2:
        return li

    low, same, high = [], [], []

    pivot = li[randint(0, n - 1)]

    for t, el in enumerate(li):
        plt.bar(X, li, color=(0.2, 0.4, 0.6, 0.6))
        plt.title(f"Number of operations: {number_of_operations}")
        number_of_operations += 1
        plt.pause(delay)
        plt.clf()
        if el < pivot:
            low.append(el)
            li[t] = 0
        elif el == pivot:
            same.append(el)
            li[t] = 0
        elif el > pivot:
            high.append(el)
            li[t] = 0

    result = quicksort(low, x, delay, number_of_operations, type="low") + same + quicksort(high, x, delay, number_of_operations, type="high")
    if len(result) == len(x):
        color = ['cyan' for i in low] + [(0.2, 0.4, 0.6, 0.6) for i in same] + ['blue' for i in high]
        color[result.index(pivot)] = 'red'
        plt.bar(x, result, color=color)
        plt.title(f"Number of operations: {number_of_operations} - Pivot: Red")
        plt.show()
    return result

def bogo_sort(li, x, delay, number_of_operations=0):
    def is_sorted(li):
        for i in range(0, len(li) - 1):
            if li[i] > li[i+1]:
                return False
        return True
    
    while not is_sorted(li):
        plt.bar(x, li, color=(0.2, 0.4, 0.6, 0.6))
        plt.title(f"Number of operations: {number_of_operations}")
        number_of_operations += 1
        plt.pause(delay)
        plt.clf()
        shuffle(li)

    plt.bar(x, li, color=(0.2, 0.4, 0.6, 0.6))
    plt.title(f"Number of operations: {number_of_operations}")
    plt.show()
def merge_sort(li, x, delay, number_of_operations=0):
    if len(li) > 1:
        mid = len(li) // 2
        left_half = li[:mid]
        right_half = li[mid:]

        merge_sort(left_half, x, delay, number_of_operations)
        merge_sort(right_half, x, delay, number_of_operations)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                li[k] = left_half[i]
                i += 1
            else:
                li[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            li[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            li[k] = right_half[j]
            j += 1
            k += 1

        plt.bar(x, li, color=(0.2, 0.4, 0.6, 0.6))
        plt.title(f"Number of operations: {number_of_operations}")
        number_of_operations += 1
        plt.pause(delay)
        plt.clf()

    return li

def heapify(li, n, i, x, delay, number_of_operations):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and li[i] < li[left]:
        largest = left

    if right < n and li[largest] < li[right]:
        largest = right

    if largest != i:
        li[i], li[largest] = li[largest], li[i]
        plt.bar(x, li, color=(0.2, 0.4, 0.6, 0.6))
        plt.title(f"Number of operations: {number_of_operations}")
        number_of_operations += 1
        plt.pause(delay)
        plt.clf()
        heapify(li, n, largest, x, delay, number_of_operations)

def heap_sort(li, x, delay):
    n = len(li)
    number_of_operations = 0

    for i in range(n, -1, -1):
        heapify(li, n, i, x, delay, number_of_operations)

    for i in range(n-1, 0, -1):
        li[i], li[0] = li[0], li[i]
        heapify(li, i, 0, x, delay, number_of_operations)

    plt.bar(x, li, color=(0.2, 0.4, 0.6, 0.6))
    plt.title(f"Number of operations: {number_of_operations}")
    plt.show()

    return li
