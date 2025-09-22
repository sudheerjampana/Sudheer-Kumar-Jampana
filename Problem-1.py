# Problem 1: Simple Calculator
class Calculator():
    def __init__(self,a,b,operation):
        self.a=a
        self.b=b
        self.op=operation
    def operation(self):
        if self.op=="Addition" or self.op=="+":
            return f"Addition of {a} and {b} is => {self.a+self.b}"
        elif self.op=="Subtraction" or self.op=="-":
            return f"Subtraction of {a} and {b} is => {self.a-self.b}"
        elif self.op=="Multiplication" or self.op=="*":
            return f"Multiplication of {a} and {b} is => {self.a*self.b}"
        elif self.op=="Division" or self.op=="/":
            try:
                return f"Division of {a} and {b} is => {self.a/self.b}"
            except Exception as e:
                return f"Error: {e}"
        else:
            return ("Invalid Operation")
a=float(input("enter a value: "))
b=float(input("enter b value: "))
operator=input("enter type of operation: ")

obj=Calculator(a,b,operator)
print(obj.operation())

        