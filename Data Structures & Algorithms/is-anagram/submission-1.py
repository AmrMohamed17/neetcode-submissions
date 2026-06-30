class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) > len(s):
            s, t = t, s
        for letter in s:
            if letter not in t:
                return False
            
            t = t.replace(letter, "", 1)

        return True
        