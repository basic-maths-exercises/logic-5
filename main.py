import numpy as np

def numberOutside( data, a, b ) : 
  # You need to write code here



# This code allows you to see if your functions are working correctly
data = np.loadtxt("mydata.dat")
print( numberOutside(data,2,5), "of the integers in mydata.dat are not between 2 and 5" )
print( numberOutside(data,5,9), "of the integers in mydata.dat are not between 5 and 9" )
