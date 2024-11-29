class Calculator():
    def __init__(self,a,b,opr):
        self.a=a
        self.b=b
        self.opr=opr
    def cal(self):
        if self.opr == "+":
            return self.a+self.b
        elif self.opr == "-":
            return self.a-self.b
        elif self.opr =="*":
            return self.a*self.b
        elif self.opr =="/":
            return self.a/self.b
        elif self.opr =="%":
            return self.a%self.b
        

cal1=Calculator(6,5,"%")
print(cal1.cal())
