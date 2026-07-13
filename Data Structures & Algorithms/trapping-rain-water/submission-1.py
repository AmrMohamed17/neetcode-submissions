class Solution:
    def trap(self, height: List[int]) -> int:
        trapped_water = 0
        l, r = 0, len(height) - 1
        left_max, right_max = height[l], height[r]

        while l < r:
            if left_max < right_max:
                l += 1
                left_max = max(left_max, height[l])
                water = left_max - height[l]
                if water > 0:
                    trapped_water += water
                
            else:
                r -= 1
                right_max = max(right_max, height[r])
                water = right_max - height[r]
                if water > 0:
                    trapped_water += water
                    
        return trapped_water