def start_p(arr, x, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == x:
            if mid - 1 < 0 or arr[mid - 1] != x:
                # 첫번째 인덱스일 경우 또는 앞의 원소값이 x가 아닐 경우 => x의 첫번째 인덱스
                return mid
            else:
                # 위의 조건에 맞지 않는 경우, 첫번째 위치가 아니기 때문에 현재 x값의 앞을 end 로 넣어줌
                end = mid - 1
        elif arr[mid] >= x:
            end = mid - 1
        else:
            start = mid + 1
    return -1


def last_p(arr, x, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == x:
            if mid + 1 >= N or arr[mid + 1] != x:
                # 마지막 인덱스일 경우 또는 뒤의 원소값이 x가 아닐 경우 => x의 마지막 인덱스
                return mid + 1
            else:
                # 위의 조건에 맞지 않는 경우, 마지막 위치가 아니기 때문에 현재 x값의 뒤를 start 로 넣어줌
                start = mid + 1
        elif arr[mid] > x:
            end = mid - 1
        else:
            start = mid + 1
    return -1


N, x = map(int, input().split())
arr = list(map(int, input().split()))

if start_p(arr, x, 0, N - 1) == -1:
    print(-1)
else:
    print(last_p(arr, x, 0, N - 1) - start_p(arr, x, 0, N - 1))

# from bisect import bisect_left, bisect_right
#
#
# def solution(arr, start_p, end_p):
#     start = bisect_left(arr, start_p)  # x의 첫 인덱스
#     end = bisect_right(arr, end_p)  # x의 마지막 인덱스
#     return end - start
#
#
# N, x = map(int, input().split())
# arr = list(map(int, input().split()))
# result = solution(arr, x, x)
# if result == 0:
#     print(-1)
# else:
#     print(result)





