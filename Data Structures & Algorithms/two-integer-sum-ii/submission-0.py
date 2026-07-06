class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashset = {}

        for idx, num in enumerate(numbers):
            ind = hashset.get(num, -1)
            print(ind)
            if ind == -1:
                print("idx", idx)
                print("target - num", target - num)
                hashset[target - num] = idx
            else:
                return [ind + 1, idx + 1] 

        print(hashset)
        return []