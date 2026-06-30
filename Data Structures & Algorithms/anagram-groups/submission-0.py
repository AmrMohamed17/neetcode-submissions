from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        similars = defaultdict(list)

        for string in strs:
            string_sort = "".join(sorted(string))
            similars[string_sort].append(string)

        
        return list(similars.values())