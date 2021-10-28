import sys


def push(x):
    stack.append(x)


def pop():
    if not stack:
        return -1
    else:
        return stack.pop()


def size():
    return len(stack)


def empty():
    return 0 if stack else 1


def top():
    return stack[-1] if stack else -1


N = int(sys.stdin.readline().rstrip())
stack = []
for _ in range(N):
    command = sys.stdin.readline().rstrip().split()

    cmd = command[0]

    if cmd == "push":
        push(command[1])
    elif cmd == "pop":
        print(pop())
    elif cmd == "size":
        print(size())
    elif cmd == "empty":
        print(empty())
    elif cmd == "top":
        print(top())
