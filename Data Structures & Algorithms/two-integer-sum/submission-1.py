class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        test = {}

        for idx, num in enumerate(nums):
            if test.get(num, -1) == -1:
                test[target - num] = idx
            else:
                return [test[num], idx]