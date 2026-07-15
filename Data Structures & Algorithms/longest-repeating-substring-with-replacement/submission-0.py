class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = []
        max_window = 0

        for ch in range(len(s)):
            window.append(s[ch])
            freq = Counter(window).most_common(1)[0][1]
            if len(window) - int(freq) > k:
                window.pop(0)
            else:
                max_window = max(max_window, len(window))


        
        return max_window

        
        