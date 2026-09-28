class Solution:
    def calPoints(self, operations: List[str]) -> int:

        stk = []
        for op in operations:
            if op == "+":
                stk_c = stk.copy()
                num1 = stk_c.pop()
                num2 = stk_c.pop()
                res = num1 + num2
                stk.append(res)
            elif op == "D":
                numi = stk.pop()
                num = numi * 2
                stk.append(numi)
                stk.append(num)
            elif op == "C":
                stk.pop()
            else:
                stk.append(int(op))
        return sum(stk)

        