import pandas as pd
import numpy as np

print np.zeros(10)
print np.empty((2, 3, 2))

arr1 = np.array([1, 2, 3], dtype=np.float64)
print "arr1 ",arr1

arr2 = np.array([1, 2, 3], dtype=np.int32)
print "arr2 ",arr2

float_arr = arr2.astype(np.float64)
print "float arr2 ",float_arr

arr = np.arange(10)
print arr
print arr[5:8]
print ":3 ", arr[:3]
print "3: ",arr[3:]

arr3d = np.array([[1 , 2, 3],
                [4,5,6],
                [7,8,9]    ])
print arr3d
print arr3d.shape
print ":1,1: ", arr3d[:1,1:]
print ":2,2: ", arr3d[:2,2:]
print ":1,2: ", arr3d[:1,2:]
print "1:2,1:2 ", arr3d[1:2,1:2 ]



