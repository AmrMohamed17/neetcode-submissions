class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = "".join(sorted(s1))

        l, r = 0, len(s1)

        while r <= len(s2):
            part = s2[l: r]
            part = "".join(sorted(part))
            print(f"{l}: ", part, s1)

            if part == s1:
                return True

            l += 1
            r += 1


        return False

        
        