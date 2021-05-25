from SparseMatrix import *
import numpy as np

sp1 = SparseMatrix(3, 4)
sp1.insert(0, 0, 1)
sp1.insert(1, 2, 1)
sp1.insert(2, 2, 3)
sp1.insert(2, 3, 4)
# print('SP 1:')
# print(sp1)


sp2 = SparseMatrix(3, 4)
sp2.insert(1, 1, 2)
sp2.insert(1, 2, 3)
# print('SP 2:')
# print(sp2)

sp3 = SparseMatrix(3, 4)
sp3.insert(0, 1, 1)
sp3.insert(1, 0, 1)
sp3.insert(0, 2, 0)
sp3.insert(2, 0, 0)
# print('SP 3:')
# print(sp3)

sum_sp = sp1.add(sp2)
print('Summation: ')
print(sum_sp)

print("Transpose: ")
print(sp1.transpose())


multiplicand_sp = np.matrix(sp3.__matrix__).transpose()
multiplicand_sp.shape
multiplier_sp = np.matrix(sp3.__matrix__)
multiplier_sp.shape
print('Multiplication: ')
print(multiplicand_sp * multiplier_sp)


