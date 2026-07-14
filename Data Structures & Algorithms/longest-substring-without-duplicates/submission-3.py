class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        longest_substring = ""
        count = 1

        for ch in s:
            if ch not in longest_substring:
                longest_substring += ch
            else:
                count = max(count, len(longest_substring))
                index = longest_substring.find(ch)
                longest_substring = longest_substring[index + 1:] + ch

        
        count = max(count, len(longest_substring))
        return count

        