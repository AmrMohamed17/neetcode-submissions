class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, finish = 0, len(nums) - 1

        mid = (start + finish + 1) // 2

        while start <= finish:
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                finish = mid - 1
            else:
                start = mid + 1
            
            mid = (start + finish + 1) // 2



        return -1 

        