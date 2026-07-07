class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()
        length = len(nums)

        for idx in range(length):
            l, r = idx + 1, length - 1
            while l < r:
                triplet = nums[l] + nums[r] + nums[idx]
                if triplet == 0:
                    triplets.append([nums[l], nums[r], nums[idx]])
                    l += 1
                elif triplet > 0:
                    r -= 1
                else:
                    l += 1
            
                    
               

        print(triplets)
        unique_triplets = []
        seen = set()
        for triplet in triplets:
            triplet.sort()

            unique_tuple = tuple(triplet)
            if unique_tuple not in seen:
                seen.add(unique_tuple)
                unique_triplets.append(triplet)

        
        return unique_triplets

        


        