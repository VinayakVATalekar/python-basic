class car:  
    def __init__(self,modelname, year):  
        self.modelname = modelname  
        self.year = year  
    def display(self):  
        print(self.modelname,self.year)  
  
c1 = car("Toyota", 2016)  
c1.display()  

class Employee:    
    id = 10   
    name = "John"    
    def display (self):    
        print("ID: %d \nName: %s"%(self.id,self.name))    
# Creating a emp instance of Employee class  
emp = Employee()    
emp.display()    
