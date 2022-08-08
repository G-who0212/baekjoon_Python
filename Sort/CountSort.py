array = [7, 5, 5, 5, 7, 9, 0, 9, 3, 1]

count = [0] * (max(array) + 1)
for i in array:
    count[i] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')