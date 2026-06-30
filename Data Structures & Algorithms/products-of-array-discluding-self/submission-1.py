import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = []

        for idx, num in enumerate(nums):
            tmp = nums.copy()
            del tmp[idx]
            products.append(math.prod(tmp))

        return products
        