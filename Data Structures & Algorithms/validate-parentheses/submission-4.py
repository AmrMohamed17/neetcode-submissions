class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        hash_map = {')': '(', ']': '[', '}': '{'}

        for ch in s:
            if ch == '(' or ch == '[' or ch == '{':
                stack.append(ch)
            else:
                if not stack:
                    return False
                popped = stack.pop()
                if popped != hash_map[ch]:
                    return False

        print(stack)
        if stack:
            return False
        
        return True

        