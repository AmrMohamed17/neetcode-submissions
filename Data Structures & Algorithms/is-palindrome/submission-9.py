class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char.lower() for char in s if char.isalnum())
        print(s)
        
        end = len(s) - 1
        print(end)
        for start in range(len(s)):
            if s[start] == s[end]:
                end -= 1
            else:
                print()
                return False

        
        return True

            
        