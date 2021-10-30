import sys

T = int(sys.stdin.readline())

for i in range(T):
    test = sys.stdin.readline().rstrip()
    stack = []
    for j in range(len(test)):
        if test[j] == "(":
            stack.append(test[j])
        elif test[j] == ")":
            if len(stack) != 0 and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(test[j])

    if len(stack) == 0:
        print("YES")
    else:
        print("NO")




