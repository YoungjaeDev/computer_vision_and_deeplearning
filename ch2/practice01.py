import numpy as np

a = np.array([400, 52, 'tiger', '24', 230])

print(a)
print(type(a))
print(a.shape)
# 모든 원소를 str 타입으로 해석
a.sort()
print(a)
