import numpy as np
# to check version
print("version", np.__version__)
# create 1-D array with range of 0 to 9
print(np.arange(10))
a = np.arange(10)
print("0-9",a)
# create a 3X3 array with all True's
print("3X3", np.full((3,3), True, dtype=bool))
print("3X3", np.ones((3,3), dtype=bool))
# get all the odd numbers in a array
print("odd numbers", a[a%2==1])
# replace all the odd numbers to -1 in in an array
a[a%2==1] = -1
print("odd to -1", a)
# replace all the odd with -1 without changing the array
print("odd to -1 using where", np.where(a%2==1, -1, a))
# convert 1-D array to 2-D array
print("1-D to 2-D", a.reshape(2,5))
# vertical and horizontal stack of 2-D array
x = np.arange(10).reshape(2,5)
y = np.repeat(1,10).reshape(2,5)
#vertical
print("vertical", np.concatenate([x,y], axis=0))
print("vertical", np.vstack([x,y]))
print("vertical", np.r_[x,y])
#horizontal
print("horizontal", np.concatenate([x,y], axis=1))
print("horizontal", np.hstack([x,y]))
print("horizontal", np.c_[x,y])
# creating a pattern of [1 1 1 2 2 2 3 3 3 1 2 3 1 2 3 1 2 3] without hardcoding
z = np.array([1,2,3])
# print(z)
print("pattern creation", np.r_[np.repeat(z,3),np.tile(z,3)])
# find common items in C and D
c = np.array([1,2,3,4,5,6,7])
d = np.array([6,3,2,4,8.9,10])
print(np.intersect1d(c,d))
# remove items of c present in d
print(np.setdiff1d(c,d))
# common position of mathcing element in c and d 
print(np.where(c==d)) # this wiil be deprecated in futue
# get all items between 5 and 10 in a 15 index array
a = np.arange(15)
print(np.where((a>=5) & (a<=10)))
print(np.where(np.logical_and((a>=5), (a<=10))))
print(a[(a>=5) & (a<=10)])
# swap columns & rows 1 and 2 
a = np.arange(9).reshape(3,3)
print(a)
#columns swap
print(a[:,[1,0,2]])
# row swap
print(a[[1,0,2],:])
#reverse a array by rows
print(a[::-1])
#reverse array by columns
print(a[:,::-1])
# random floating digit from 5 to 10 with 3X5 array
print(np.random.randint(low=5,high=10,size=(5,3))+np.random.random((5,3)))
print(np.random.uniform(5,10, size=(5,3)))

