import math
num, max_room = map(int, input().split())
#0~5:여학생, #6~11:남학생
stu_num = {x: 0 for x in range(12)}
count = 0
for i in range(num):
    S, grade = map(int, input().split())
    if S == 0:
        stu_num[grade-1] += 1
    else:
        stu_num[grade+5] += 1

for i in range(12):
    if stu_num[i] > max_room:
        # 나눈 수의 몫 + 나머지가 있다면 +1 을 위해 올림
        count += math.ceil(stu_num[i]/max_room)
    elif stu_num[i] == 0:
        continue
    else:
        count += 1

print(count)
