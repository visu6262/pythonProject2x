# swap two numbers with calss
class swap():
    def __init__(self):
        self.num1=int(input("Enter Number 1:"))
        self.num2=int(input("Enter Number 2:"))
        print(f"Before Swap\nNumber1:{self.num1}\nNumber2:{self.num2}")
    def output(self):
        temp=self.num1
        self.num1 = self.num2
        self.num2 = temp
        print(f"After Swap\nNumber1:{self.num1}\nNumber2{self.num2}")
outobj=swap()
outobj.output()