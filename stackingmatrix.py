import numpy as np

a = np.array([1,2,3,4,5])
b = np.array([6,7,8,9,10])

aMat = np.zeros((2,2))
bMat = np.ones((2,3))

c = np.hstack((a,b))
d = np.vstack((a,b))

cMat = np.hstack((aMat,bMat))
print(cMat)