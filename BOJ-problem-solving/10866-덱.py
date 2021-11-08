import sys
from collections import deque


def push_front(x):
    Deque.appendleft(x)


def push_back(x):
    Deque.append(x)


def pop_front():
    if Deque:
        return Deque.popleft()
    else:
        return -1


def pop_back():
    if Deque:
        return Deque.pop()
    else:
        return -1


def size():
    return len(Deque)


def empty():
    if not Deque:
        return 1
    else:
        return 0


def front():
    if Deque:
        return Deque[0]
    else:
        return -1


def back():
    if Deque:
        return Deque[-1]
    else:
        return -1


N = int(sys.stdin.readline())
Deque = deque()
for i in range(N):
    d = sys.stdin.readline().split()
    cmd = d[0]

    if d[0] == 'push_front':
        push_front(d[1])
    elif d[0] == 'push_back':
        push_back(d[1])
    elif d[0] == 'pop_front':
        print(pop_front())
    elif d[0] == 'pop_back':
        print(pop_back())
    elif d[0] == 'size':
        print(size())
    elif d[0] == 'empty':
        print(empty())
    elif d[0] == 'front':
        print(front())
    elif d[0] == 'back':
        print(back())
