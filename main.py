

def binary_search(list, item):
    # бинарный поиск - это алгоритм; на входе он получает отсортированный список элементов.
    # если элемент, который вы ищете, присутствует в списке, то бинарный поиск возвращает
    # его индекс. в противном случае возвращает null
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

    # бинарный поиск работает намного быстрее простого
    # время выполнения O(log n) быстрее O(n), а с увеличением списка оно становится намного быстрее


my_list = [1, 5, 10, 11, 12, 15]
my_list = [int(x) for x in my_list]
print(binary_search(my_list, 12))
print(binary_search(my_list, 1))


def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[1]
            smallest_index = i
    return smallest_index


def selectSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr


def gbt_selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        min_index = i

        # Find the index of the minimum element in the unsorted part of the array
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum element with the first element in the unsorted part
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


print(selectSort([5, 2, 6, 1, 3, 10]))


def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[len(array) // 2]
        less = [i for i in array if i < pivot]
        middle = [i for i in array if i == pivot]
        greater = [i for i in array if i > pivot]
        return quicksort(less) + middle + quicksort(greater)


print(quicksort([10, 5, 2, 3]))



