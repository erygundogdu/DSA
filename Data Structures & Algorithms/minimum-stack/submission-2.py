class MinStack:

    def __init__(self):
        self.stk = []
        self.m_stk = []
        

    def push(self, val: int) -> None:
        if self.stk != []:
            if val<=self.m_stk[-1]:
                self.m_stk.append(val)
        else:
            self.m_stk.append(val)
        self.stk.append(val)

    def pop(self) -> None:
        if self.stk != []:
            elem = self.stk.pop()
        if self.m_stk[-1] == elem:
            self.m_stk.pop()
    def top(self) -> int:
        if self.stk != []:
            return self.stk[-1]
    def getMin(self) -> int:

        if self.m_stk != []:
            return self.m_stk[-1]
        
