class Employee:  
    __count = 0;#here __ gives the abtraction so no object can see this gives error   
    def __init__(self):  
        Employee.__count = Employee.__count+1  
    def display(self):  
        print("The number of employees",Employee.__count)  
emp = Employee()  
emp2 = Employee()  
try:  
    print(emp.__count) #errror here cause __count is private 
finally:  
    emp.display()  
