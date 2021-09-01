import bisect
#1 재귀이용
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(left, right):
            if left <= right:
                mid = left + (right - left) // 2
                if nums[mid] < target:
                    return binary_search(mid + 1, right)
                elif nums[mid] > target:
                    return binary_search(left, mid - 1)
                else:
                    return mid
            else:
                return -1

        return binary_search(0, len(nums) - 1)
#2 이진 검색 사용
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index = bisect.bisect_left(nums, target)

        if index < len(nums) and nums[index] == target:
            return index
        else:
            return -1
#3 이진 검색x index 풀이

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except ValueError:
                return -1