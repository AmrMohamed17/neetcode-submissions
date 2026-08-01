import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            # Use lambda for truncation toward zero division (required by LeetCode)
            "/": lambda a, b: int(a / b) 
        }

        stack = deque()

        for token in tokens:
            if token in ops:
                num1 = stack.pop()
                num2 = stack.pop()

                result = ops[token](num2, num1)
                stack.append(result)
            else:
                stack.append(int(token))

        
        return stack.pop()


        