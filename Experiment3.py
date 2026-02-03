#1:WAP to creae numpy array:
import numpy
arr = numoy.array([1,2,3,4])
print(arr)

#2:WAP to create a nummpy aarray aand perform different operations like +,*  & ^:
import numpy
arr = numpy.array([1,2,3,4])
print(arr[1] + arr[2])
print(arr[1]*arr[2])
print(arr([1]^arr[2]))

#3:WAP to create numpy array and perform array indexing and slicing:
import nummpy as np
arr = np.array([[1,2,3,4],5,[6,7,8,9,10]])
print(arr)
print("The element in the 1st row and 2nd column :",arr[0,1])
print("Slicing first two rows:")
print(arr[0:2,:])

#4:WAP to create numpy array and perform matrix multiplication:
import numpy as np
a = np.array([1,2,3],
             [4,5,6])
b = np.array([1,3,5],
             [2,4,6])
print(a)
print(b)
result = np.multiply(a,b)
print(result)

#5:WAP to find minimum and maximum
import numpy as np
arr = np.array({1,2,3,4,5,6,78,})
print(arr)
min = np.min(arr)
print(min)
max = np.max(arr)
print(max)

#6:WAP to concatenate and stacking:
import numpy as np
arr = np.array([1,2,3,4,5,6])
arr2 = np.array([10,20,30,40,50,60])
print("Array 1 is: ",arr)
print("Array 2 is: ",arr2)
concat = np.concatenate(arr,arr2)
print(concat)
stack = np.stack(arr,arr2)
print(stack)

#7:WAP to element wise comparision:
import numpy as np
a = np.array([10,20,30,40,50])
b = np.array([15,20,25,30,50])
print("Array a:",a)
print("Array b :",b)
print("A>B:",a>b)
print("A<B:",a<b)
print("A==B:",a==b)