class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i , j in enumerate(nums):
            number_need = target - j
            if number_need in seen:
                return[seen[number_need],i]
            seen[j] = i
        