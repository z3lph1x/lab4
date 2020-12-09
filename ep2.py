from scipy import linalg
import matplotlib.pyplot as plt
import numpy as np

with open('large.txt', 'r') as f:
	mtrx = f.read().splitlines()
n = int(mtrx[0])
b = []
A = np.zeros((n,n))
for i in range(1,n+1):
	mtrx[i] = mtrx[i].split(' ')
	for j in range(n):
		A[i-1,j] = float(mtrx[i][j])
b = mtrx[n+1].split(' ')
for i in range(n):
	b[i] = float(b[i])
print(A)
print(b)
fig, ax=plt.subplots()
ax.bar(np.arange(n), linalg.solve(A,b))
ax.grid()
plt.show()
