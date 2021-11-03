import sys
from collections import deque


def push(x):
    Queue.append(x)


def pop():
    if not Queue:
        return -1
    else:
        return Queue.popleft()


def size():
    return len(Queue)


def empty():
    if not Queue:
        return 1
    else:
        return 0


def front():
    if not Queue:
        return -1
    else:
        return Queue[0]


def back():
    if not Queue:
        return -1
    else:
        return Queue[-1]


N = int(sys.stdin.readline().rstrip())
Queue = deque([])

for _ in range(N):
    t = sys.stdin.readline().rstrip().split()

    cmd = t[0]

    if cmd == "push":
        push(t[1])
    elif cmd == "pop":
        print(pop())
    elif cmd == "size":
        print(size())
    elif cmd == "empty":
        print(empty())
    elif cmd == "front":
        print(front())
    elif cmd == "back":
        print(back())
