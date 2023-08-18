class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        operators = '+-/*'
        for t in tokens :
            if t not in operators: 
                stack.append(int(t))
            else :
                second = stack.pop()
                first = stack.pop()
                if (t == '+'):
                    stack.append(first + second)
                elif (t == '-'):
                    stack.append(first - second)
                elif (t == '*'):
                    stack.append(first * second)
                elif (t == '/'):
                    stack.append(int(float(first)/ second))
        return stack.pop()
