class Solution:
    def isPalindrome(self, s: str) -> bool:
        forward, backward = [], []
        for letter in s:
            if letter.isalpha() or letter.isdigit():
                letter = letter.lower() if letter.isalpha() else letter
                forward.append(letter)
                backward.insert(0, letter)

        
        print(forward)
        print(backward)
        return forward == backward
            
        