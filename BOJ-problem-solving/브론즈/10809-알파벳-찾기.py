s = input()
a = [-1 for i in range(26)]  # 알파벳 숫자개수 만큼 -1을 넣어준다
for i in range(len(s)):
    n = (ord(s[i]) - 97)  # 아스키 코드로 변환 후 97을 빼서 자릿수를 맞춘다
    if a[n] == -1:  # -1이라면 처음으로 나온 위치인 i로 바꿔준다
        a[n] = i

for i in range(len(a)):
    print(a[i], end=' ')