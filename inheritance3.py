class Cal1:  
    def Summation(self,a,b):  
        return a+b;  
class Cal2:  
    def Multiplication(self,a,b):  
        return a*b;  
class Derived(Cal1,Cal2):  
    def Divide(self,a,b):  
        return a/b;  
d = Derived()  
print(d.Summation(10,20))  
print(d.Multiplication(10,20))  
print(d.Divide(10,20))  
