from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        for n, c in count.items():
            freq[c].append(n)

        top_k = []
        for nums in reversed(freq):
            for num in nums:
                top_k.append(num)

                if len(top_k) == k:
                    return top_k

        