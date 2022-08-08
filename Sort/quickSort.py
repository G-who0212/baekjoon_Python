array = [7, 5, 9, 0, 3, 1]

def quickSort(array, start, end):
    if start >= end: return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[right], array[left] = array[left], array[right]
    quickSort(array, start, right-1)
    quickSort(array, right + 1, end)
    
quickSort(array, 0, len(array)-1)
print(array)