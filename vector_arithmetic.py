import numpy as np

a = np.array([20,40,60])
b = np.array([10,20,30])
c = np.array([5,10,15,20])

# Dimensions are the same
print(a+b)
print(a-b)

# Error because dimensions are not the same
# print(a+c)

# Multiplication / division of the same vectors if they have the same length
print(a*b)
print(a/b)

# Vector Scalar Multiplication
scalar=2
list_a=[10,11,12,13,14,15]
print(list_a)

list_as_array = np.array(list_a)
print(list_as_array)

# We get the same list twice 
print(scalar*list_a)
# We get the vector scalar multiplication
print(scalar*list_as_array)

