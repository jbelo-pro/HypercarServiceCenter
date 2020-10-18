from collections import deque

n = int(input())
my_queue = deque()
for t in [input() for x in range(n)]:
    if t == 'DEQUEUE':
        my_queue.pop()
    else:
        my_queue.appendleft(t)

while len(my_queue):
    print(str.split(my_queue.pop(), ' ')[1])
