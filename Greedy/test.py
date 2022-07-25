from collections import deque

queue1 = deque()
queue1.append(1)
queue1.append(3)
queue1.append(5)

queue2 = deque([1])
queue2.append(3)
queue2.append(5)

print(queue1)
print(queue2)