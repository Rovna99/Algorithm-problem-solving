S = input().upper()  # 대소문자 구분이 없고, 답 출력이 대문자이기에 대문자로 통일
word = list(set(S))  # 단어 중복 없이, 순서대로 넣기위해 set 사용
result = []  # 갯수를 세기 위함
for i in word:
    result.append(S.count(i))  # 몇 개 나오는지 세어서 값 저장(같은 순서)

if result.count(max(result)) > 1:  # 최대개수가 같은 것이 있다면 ? 출력
    print("?")
else:  # 아니면 result의 인덱스(word의 순서랑 같음)으로 word에서 단어 출력
    print(word[result.index(max(result))])

