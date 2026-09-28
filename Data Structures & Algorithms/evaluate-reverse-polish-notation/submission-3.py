class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []

        for t in tokens:
            if t == "+":
                num1 = stk.pop()
                num2 = stk.pop()
                res = int(num1) + int(num2)
                stk.append(res)
            elif t == "-":
                num1 = stk.pop()
                num2 = stk.pop()
                res = int(num2) - int(num1)
                stk.append(res)
            elif t == "*":
                num1 = stk.pop()
                num2 = stk.pop()
                res = int(num1) * int(num2)
                stk.append(res)
            elif t == "/":
                num1 = stk.pop()
                num2 = stk.pop()
                res = int(num2) / int(num1)
                stk.append(res)
            else:
                stk.append(int(t))
        return int(stk[0])