reversed_queue = deque()

while len(queue):
    reversed_queue.appendleft(queue.popleft())
