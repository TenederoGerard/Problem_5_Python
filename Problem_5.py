import numpy as np
import matplotlib.pylab as plt

n=np.linspace(0,199,200);       
def x(n): 

#Eval function to make 'String' to return as integer. 
    e=eval(a); 
    return e 

a = (input("Enter Equation:"));   
 
for i in range(0,200): 
    if i == 0:
        y = (-1.5*x(n)) + (2*x(n+1)) - (0.5*x(n+2));
        
    elif i == 199:
        y = (1.5*x(n)) - (2*x(n-1)) + (0.5*x(n-2));
        
    else:
        y = (0.5*x(n+1))-(0.5*x(n-1));

plt.title('Problem 5')
plt.plot(x(n), label = 'x(n)')
plt.xlabel('x(n)')

plt.plot(y, label = 'y(n)')
plt.ylabel('y(n)')
plt.legend()
plt.grid(True)
plt.show()