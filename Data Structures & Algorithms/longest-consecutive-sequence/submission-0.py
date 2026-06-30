class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = {}

        for num in nums:
            hashset[num] = 1
        
        maximum = 0
        for num in nums:
            if hashset.get(num-1, 0) == 0:
                tmp, count = num, 1
                while True:
                    tmp += 1
                    if hashset.get(tmp, 0):
                        count += 1
                    else:
                        maximum = count if count > maximum else maximum
                        break
        
        return maximum
                
            

        