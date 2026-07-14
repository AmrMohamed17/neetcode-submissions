class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        max_len = 0
        left = 0

        for right, ch in enumerate(s):
            if ch in char_map and char_map[ch] >= left:
                left = char_map[ch] + 1

            char_map[ch] = right

            max_len = max(max_len, right - left + 1)

        return max_len


        