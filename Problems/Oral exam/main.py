from collections import deque

n = int(input())
my_queue = deque()
for t in [input() for x in range(n)]:
    if t == 'PASSED':
        print(str.split(my_queue.pop(), ' ')[1])
    elif t == 'EXTRA':
        my_queue.appendleft(my_queue.pop())
    else:
        my_queue.appendleft(t)
