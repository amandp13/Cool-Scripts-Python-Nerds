# Program to plot a quadratic function
import matplotlib.pyplot as plt
import numpy as np

print("Equation is in the form of a*x^2+b*x+c=0")
print("Range of x is (-30,30)")
print("Enter value of a")
a=int(input())
print("Enter value of b")
b=int(input())
print("Enter value of c")
c=int(input())

x=np.arange(-30,30)
y=a*(x**2)+b*x+c
plt.plot(x,y,label="f(n)")
plt.grid()
plt.show()
