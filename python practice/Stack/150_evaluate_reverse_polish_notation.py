# 150. Evaluate Reverse Polish Notation
# Evaluate the value of an arithmetic expression in Reverse Polish Notation.

# Valid operators are +, -, *, /. Each operand may be an integer or another expression.

# Some examples:
#   ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
#   ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6


class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        i = 0
        while i < len(tokens) :
            if tokens[i] in ['+', '-', '*', '/']:
                try:
                    num2 = stack.pop()
                    num1 = stack.pop()
                    print num1, num2
                    print tokens[i]
                    if tokens[i] == '+':
                        stack.append(num1 + num2)
                    if tokens[i] == '-':
                        stack.append(num1 - num2)
                    if tokens[i] == '*':
                        stack.append(num1 * num2)
                    if tokens[i] == '/':
                        if num2 * num1 < 0:
                            stack.append(-(abs(num1) / abs(num2)))
                        else:
                            stack.append(num1 / num2)
                except:
                    return -99
            else:
                stack.append(int(tokens[i]))
            i += 1
        if len(stack) == 1:
            return stack.pop()
        else:
            return -99

# print Solution().evalRPN(["0", "3", "/"])
print Solution().evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5","+"])