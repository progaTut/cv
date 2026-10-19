# a = []
# for i in range(1,1000001):
#     a.append(i)
# print(a)

import numpy as np
# b = np.arange(0,1000001)
# print(b)

qq = []
for i in range(1 ,1000):
    qq.append(10000000000 + i)
aa = []
for j in range(1 ,1000):
    aa.append(qq)
print(aa)

import numpy as np
bb = np.full((1000,1000), 1000000) 
print(bb)