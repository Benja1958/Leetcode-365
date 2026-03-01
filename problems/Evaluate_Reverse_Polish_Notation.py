from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #we are using a stack to implement 
        #step 1: we append all non arithmetic ops
        #step 2: we pop last 2 elements in stack if we come across operation
        #step 3: we append the value after the operation
        #step 4: after iterating return the last value in the stack

        #helper function to get two elements from a stack
        def get_two(stack):
            second = stack.pop()
            first = stack.pop()
            return (first, second)

        stack = []
        for token in tokens:
            if token == "+":
                first, second = get_two(stack)
                res = first + second
                stack.append(res)
            elif token == "/":
                first, second = get_two(stack)
                res = int(first / second) 
                stack.append(res)
            elif token == "*":
                first, second = get_two(stack)
                res = first * second
                stack.append(res)
            elif token == "-":
                first, second = get_two(stack)
                res = first - second
                stack.append(res)
            else:
                stack.append(int(token))
        return stack[-1]




if __name__ == "__main__":
    tokens = ["2","1","+","3","*"]
    s = Solution()
    print(s.evalRPN(tokens))
