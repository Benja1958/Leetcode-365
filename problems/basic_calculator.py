class Solution:
    def calculate(self, s: str) -> int:   
        #use a stack to store previous value and sign when we ecounter an opening bracket
        #initialize values to store the sign and sign and also to get value of integers
        #if come across openning bracket, we store sign and current value, then back to default
        stack = []
        result = 0
        sign = 1
        num = 0

        #loop through the given string
        for token in s:
            #calculate the value of ints
            if token.isdigit():
                num = num * 10 + int(token)
            #get the sign for next calculation
            elif token in "-+":
                result += num * sign
                num = 0
                sign = 1 if token == "+" else -1
            #if we come across bracket, store the value in a stack
            elif token == "(":
                stack.append(result)
                stack.append(sign)
                result = 0
                num = 0
                sign = 1
            #if we come across closing bracket, we calculate the value
            elif token == ")":
                result += num * sign
                num = 0
                prev_sign = stack.pop()
                prev_res = stack.pop()
                result = prev_res + result * prev_sign
        result += num * sign
        return result

if __name__ == "__main__":
    calc = Solution()
    s = "(1+(4+5+2)-3)+(6+8)"
    print(calc.calculate(s))