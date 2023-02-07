import random
import time

global changes
global compares



def quick_sort(arrayFrom, start, end):
    if end - start > 1:
        p = partition(arrayFrom, start, end)
        quick_sort(arrayFrom, start, p)
        quick_sort(arrayFrom, p + 1, end)


def partition(arrayFrom, start, end):
    global changes
    global compares
    pivot = arrayFrom[start]
    i = start + 1
    j = end - 1

    while True:
        while i <= j and arrayFrom[i] <= pivot:
            i += 1
            compares += 1
        while i <= j and arrayFrom[j] >= pivot:
            j -= 1
            compares += 1

        if i <= j:
            arrayFrom[i], arrayFrom[j] = arrayFrom[j], arrayFrom[i]
            changes += 1
        else:
            arrayFrom[start], arrayFrom[j] = arrayFrom[j], arrayFrom[start]
            changes += 1
            return j


lst = [random.randint(0, 100) for x in range(10)]
changes = 0
compares = 0
quick_sort(lst, 0, len(lst))
print(lst, end='\n')
print(changes, compares)
