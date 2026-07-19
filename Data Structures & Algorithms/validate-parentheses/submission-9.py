class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        hash_map = {')': '(', ']': '[', '}': '{'}

        for ch in s:
            if ch in hash_map.values():
                stack.append(ch)
            else:
                if not stack or stack.pop() != hash_map[ch]:
                    return False

        return not stack

        