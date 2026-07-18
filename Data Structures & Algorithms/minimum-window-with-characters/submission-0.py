class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        min_window, min_len = "", float('inf')
        window_count, target_count = {}, {}
        for ch in t:
            target_count[ch] = target_count.get(ch, 0) + 1

        
        l= 0
        formed_unique, target_unique = 0, len(target_count)

        for r in range(len(s)):
            char = s[r]
            window_count[char] = window_count.get(char, 0) + 1
            if char in target_count and window_count[char] == target_count[char]:
                formed_unique += 1

            while formed_unique == target_unique:
                window_len = r - l + 1
                if window_len < min_len:
                    min_len = window_len
                    min_window = s[l: r + 1]

                
                window_count[s[l]] -= 1
                if s[l] in target_count and window_count[s[l]] < target_count[s[l]]:
                    formed_unique -= 1
                l += 1



        return min_window

