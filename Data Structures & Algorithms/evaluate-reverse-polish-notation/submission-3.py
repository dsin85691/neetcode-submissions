class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = [] 

        # O(n)
        for i in range(len(tokens)): 
            if len(stack) >= 2 and tokens[i] in "+-/*":
                op1, op2, res = stack.pop(), stack.pop(), None 
                if tokens[i] == "+": 
                    res = op2 + op1 
                elif tokens[i] == "-": 
                    res = op2 - op1 
                elif tokens[i] == "*": 
                    res = op1 * op2 
                elif tokens[i] == "/": 
                    res = op2 // op1 
                    if op2 % op1 != 0 and res < 0: 
                        res += 1 
                # Pop last two operands, append new res
                stack.append(res) 
            else: 
                stack.append(int(tokens[i]))

        # Final value stored on top of the stack
        return stack.pop()


