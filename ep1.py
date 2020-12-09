from scipy import linalg
from sympy import solve, Eq, symbols, Matrix
import numpy

m, p, l, lam =symbols('m p l lam')
M = numpy.array([[lam]*9]*9)
M=M-M
M[0][3]=-1/p
M[1][4]=-1/p
M[2][5]=-1/p
M[3][0]=-l-2*m
M[6][0]=-m
M[8][0]=-m
E=numpy.eye(9)
L=M-lam*E
L=Matrix(L)
d=Eq(L.det())
print(solve(d, lam))