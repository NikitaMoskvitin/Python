import numpy as np
arr = np.array([1, 78, 86.3, 4], float)
print(arr)
print(type(arr))
arr1 = np.zeros(3)
print(arr1)
arr2 = np.ones(87)
print(arr2)
arr3 = np.ones(87, dtype=np.short)
print(arr3)
print(np.linspace(1, 12, 7))
print(np.linspace(1, 13, 13))
arr4 = np.array(np.linspace(1, 12, 7), dtype=np.short)
print(arr4)
arr5 = np.arange(10, 20, 5)
print(arr5)
c = np.array([[1, 3, 5, 6], [1, 5, 8, 4]])
print(c)
d = np.array([[1, 4], [5, 6]],str)
print(d)
print(np.zeros((10,3)))
print(np.ones((4, 15),dtype=np.byte))
print(np.eye(8))
print(np.eye(4, dtype=np.short))
print(np.empty((4, 4)))
arr6 = np.random.rand(3, 5)
print(arr6)
arr7 = np.random.randint(4, 464, 3)
print(arr7)