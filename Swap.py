P = int( input("Please enter value for P: "))  
Q = int( input("Please enter value for Q: "))  
   
# To swap the value of two variables  
# we will user third variable which is a temporary variable  
temp = P  
P = Q  
Q = temp 
   
print ("The Value of P after swapping: ", P)  
print ("The Value of Q after swapping: ", Q)  
