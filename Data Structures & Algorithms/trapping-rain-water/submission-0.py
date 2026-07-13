class Solution:
    def trap(self, height: List[int]) -> int:
        trapped_water = 0
        n = len(height)

        for i in range(n):
            left_max = 0
            for j in range(i):
                left_max = max(left_max, height[j])
            
            right_max = 0
            for j in range(i + 1, n):
                right_max = max(right_max, height[j])

            water = min(left_max, right_max) - height[i]
            if water > 0:
                trapped_water += water

        return trapped_water

            





        