# Jacobi-Method

The Jacobi Method is an algorithm that is used as an Iterative Solver for linear equations; An Iterative Solver is a mathematical procedure that uses an initial guess to calculate a temporary result, and by iteration the temporary result approaches the true solution of the linear equation. This algorithm is not as complex as the Gauss Seidel (GS) algorithm which is very similar however the GS algorithm uses the next iterations values as soon as they are known unlike the Jacobi method where the value of the current iteration remains unchanged until the next iteration has been completed, this leads to the GS algorithm to converge much faster than the Jacobi Method. Furthermore, the Jacobi method makes two assumptions, one being that the system is given in the form of:

### a_11∙x_1+a_12∙x_2+⋯a_1n∙x_n=b_1
### a_21∙x_1+a_22∙x_2+⋯a_2n∙x_n=b_2
### ⋮
### a_n1∙x_1+a_n2∙x_2+⋯a_nn∙x_n=b_n

And the second being that the coefficient matrix A from the linear equation Ax = b, has no zeros on its main diagonal, namely, a_11,a_22,a_33,...,a_nn. This condition does not apply to the GS algorithm.
