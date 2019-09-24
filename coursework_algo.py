import numpy as np
from numpy.linalg import inv

# initialize the matrix
A = np.array([[15., -1., 2., 0.],
              [-1., 13., -1., 3.],
              [2., -1., 5., -1.],
              [0., 3., -1., 5.]])
# initialize the RHS vector
b = np.array([6., 25., -11., 15.])

def Jacobi_Method(A, B):

	print("\n--- The solution given by using the numpy solve function is: ---")
	print(np.linalg.solve(A, B))
	ITERATION_LIMIT = 1000
	
	D_check = np.diag(np.abs(A)) # Find diagonal coefficients
	A_check = np.sum(np.abs(A), axis=1) - D_check # Find row sum without diagonal
	
	D = np.diag(np.diag(A)) # diagonal matrix of A
	
	try:
		DIN = inv(D)
	except numpy.linalg.LinAlgError:
		print("Matrix is not invertible, try again with a different matrix")
		return
	
	R = A
	np.fill_diagonal(R, 0) # all values except the diagonal of A

	T = -1 * np.dot(DIN, R)
	C = np.dot(DIN, B)
	
	x = np.zeros_like(B) # the initial values of x
	error = np.ones_like(B)
	
	spectral = max(np.linalg.eigvals(np.dot(DIN,R))) # calculate the spectral radius of matrix A
	
	if np.all(D_check > A_check) and spectral < 1: # to check if matrix A is a valid one

		for i in range(ITERATION_LIMIT):
			x_new = np.zeros_like(x) # the values of x to be updated every iteration
			e_new = np.zeros_like(error)
			
			x_new = np.dot(T, x) + C # T and C are constant while x changes each iteration
			
			error_calc = np.dot(DIN, R) # finding the error from the calculated value to the true value 
			e_new = -1 * np.dot(error_calc, error)
			
			if np.allclose(x, x_new, atol=1e-10, rtol=0.): #check if the predicted result is no longer being changed
				break
				
			x = x_new
			error = e_new
			
		print("\n--- The Matrix A will converge using the Jacobi method to give a solution below ---\n")
		print("The Solution by the Jacobi Method is:")
		print(x)
		print("\nError")
		print(error)
		
		return
		
	else:
		print("Not a Diagonally Dominant Matrix or spectral radius is greater than 1, please change the input matrix")
		return
		
Jacobi_Method(A, b)
