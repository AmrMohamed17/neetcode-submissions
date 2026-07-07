class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        unique_triplets = []
        nums.sort()
        length = len(nums)

        for idx in range(length):
            if idx > 0 and nums[idx] == nums[idx-1]:
                continue

            l, r = idx + 1, length - 1
            while l < r:
                triplets = nums[idx] + nums[l] + nums[r]

                if triplets == 0:
                    unique_triplets.append([nums[idx], nums[l], nums[r]])
                    l,r = l + 1, r - 1
                
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                    
                    while l < r and nums[l] == nums[l-1]:
                        l += 1  
                elif triplets < 0:
                    l += 1
                else:
                    r -= 1
            

        
        return unique_triplets

        


        