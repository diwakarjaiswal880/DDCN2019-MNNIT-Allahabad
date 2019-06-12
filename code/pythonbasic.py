import numpy as np
X=np.array([12, 23, 34, 45, 56, 67, 78, 89, 90])
Y=np.array(range(54, 0, -6))

#Assignment 1 (a)
print ("X is", X)
print ("Y is", Y)
print ("Length of X is", len(X))
print ("Length of Y is", len(Y))

#Assignment 1 (b)
X_add_5 = X + 5
print ("X_add_5 is", X_add_5)

#Assignment 1 (c)
Y_times_5 = Y * 5
print ("Y_times_5 is", Y_times_5)

#Assignment 1 (d)
Sum_XY=X+Y
print ("Sum_XY is", Sum_XY)

#Assignment 1 (e)
Prod_XY=X*Y
print ("Prod_XY is", Prod_XY)

#Assignment 1 (f)
#whos use  List all the objects created along with their details in console only.

#Assignment 1 (g)
del Prod_XY

#Assignment 1 (h)
Sum_XY**(0.5)
print("Sum_XY is",Sum_XY)

#Assignment 1 (i)
Z=np.array(range(9))
Power = Y ** Z
print ("Power is", Power)

#Assignment 1 (j)
np.random.seed(111)
L =np.random.normal(123.0, 20.0, 50)
print (L)
# It will display truncated list .. L[0], L[1], .. L[49] can be printed

#Assignment 1 (k)
print (np.corrcoef(X,Y))

#Assignment 1 (l)
print ("mean of Power is ", np.mean(Power))
print ("Variance of Power is ", np.var(Power))
print ("Standard Deviation of Power is ", np.std(Power))


#Assignment 1 (m)
import matplotlib.pyplot as plt
plt.plot(X, Y_times_5,"r")
plt.xlabel('XX')
plt.ylabel('YY')
plt.savefig('/home/cloudera/Desktop/diwakar/figures/asgn1_m.pdf')
plt.show()

#Assignment 1 (n)
#From Spyder IDE(top right) browse working directory to DDCN-2019\figures
plt.plot(X, Y_times_5, 'r', X_add_5, Y, 'b--')
plt.xlabel('XX')
plt.ylabel('YY')
plt.savefig('/home/cloudera/Desktop/diwakar/figures/asgn1_n.pdf')
plt.show()

#Assignment 1 (o)
plt.plot(X, Y_times_5, 'r', X_add_5, Y, 'b--', X_add_5, Sum_XY, 'go')
plt.xlabel('XX')
plt.ylabel('YY')
plt.savefig('/home/cloudera/Desktop/diwakar/figures/asgn1_o.pdf')
plt.show()

