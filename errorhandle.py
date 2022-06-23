try:  
    a = int(input("Enter a:"))    
    b = int(input("Enter b:"))    
    c = a/b  
except:  
    print("Can't divide with zero")  
    
try:    
    a = int(input("Enter a:"))    
    b = int(input("Enter b:"))    
    c = a/b  
    print("a/b = ",c)    
# Using Exception with except statement. If we print(Exception) it will return exception class  
except Exception:    
    print("can't divide by zero")    
    print(Exception)  
else:    
    print("else block")     
