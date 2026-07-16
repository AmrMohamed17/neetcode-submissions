class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = [0] * 26
        window_count = [0] * 26

        for i in range(len(s1)):
            s1_count[ord(s1[i]) - 97] += 1
            window_count[ord(s2[i]) - 97] += 1

        if s1_count == window_count:
            return True

        for r in range(len(s1), len(s2)):
            window_count[ord(s2[r]) - 97] += 1

            l = r - len(s1)

            window_count[ord(s2[l]) - 97] -= 1

            if window_count == s1_count:
                return True

        
        return False





        
        