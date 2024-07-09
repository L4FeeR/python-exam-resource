            #always import numpy as np

import numpy as np




           #initialising an array with numpy

#1D array 
array=np.array([1,2,3,4])
print(array)
print(type(array))

#2D array
array2=np.array([[1, 2, 3], [4, 5, 6]])

#3D array
arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

#to find dimension of numpy array
#eg:
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr.ndim)

#manually mentioning array dimension
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('number of dimensions :', arr.ndim) 

#index of array

#same as normal array using []
#thuis also possible
arr = np.array([1, 2, 3, 4])
print(arr[2] + arr[3]) 

#for 2d array:
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('2nd element on 1st row: ', arr[0, 1]) 

#for 3d:
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(arr[0, 1, 2])

#negative index also works  from reverse




#slicing
#same as normal
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[:4])

#Slice from the index 3 from the end to index 1 from the end:
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[-3:-1]) 



#reshape

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
print(newarr)

#another ex for 3d
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(2, 3, 2)    #outer-->inner--->inner
print(newarr) 


#joining
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))
print(arr) 


   #axis param
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1, arr2), axis=1)
print(arr) 

   #using stack function
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.stack((arr1, arr2), axis=1)
print(arr) 

"""
#notes

comma for dimension,
colon for slicing
homogenous array
iteration possible as normal array
sorting of string is based on alphabet not length!



-----------------------------------
#Additionlas related to numpy

Splitting:

arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 4)
print(newarr) 


Search:

arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
y = np.where(arr%2 == 1)
print(x) 
print(y)

Sorting:

arr = np.array([3, 2, 0, 1])
print(np.sort(arr))


Filtering with true or false:

arr = np.array([41, 42, 43, 44])
x = [True, False, True, False]
newarr = arr[x]
print(newarr) 

#XAMPLE FOR FILTER:

Create a filter array that will return only even elements from the original array:
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

# Create an empty list
filter_arr = []

# go through each element in arr
for element in arr:
  # if the element is completely divisble by 2, set the value to True, otherwise False
  if element % 2 == 0:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]
print(filter_arr)
print(newarr) 
"""
