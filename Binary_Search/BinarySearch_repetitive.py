import sys
input = sys.stdin.readline

def binary_search_repetitive(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

n, target = map(int, input().split())
array = list(map(int, input().split()))

result = binary_search_repetitive(array, target, 0, n-1)

if(result == None):
    print("일치하는 원소가 없습니다.")
else:
    print(result + 1)