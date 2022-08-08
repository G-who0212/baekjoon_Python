array = [7, 5, 9, 0, 3, 1]

def quickSort(array):
    if len(array) <= 1:
        return array
    
    pivot = array[0]
    tail = array[1:]
    
    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]
    
    return quickSort(left_side) + [pivot] + quickSort(right_side) # 재귀

print(quickSort(array))