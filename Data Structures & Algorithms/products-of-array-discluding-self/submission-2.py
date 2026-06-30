import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        products = [1] * length
        
        # Step 1: Calculate prefix products
        # products[i] will contain the product of all numbers to the left of i
        prefix = 1
        for i in range(length):
            products[i] = prefix
            prefix *= nums[i]
            
        # Step 2: Multiply by suffix products
        # Multiply the existing prefix product by all numbers to the right of i
        suffix = 1
        for i in range(length - 1, -1, -1):
            products[i] *= suffix
            suffix *= nums[i]
            
        return products