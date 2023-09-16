import math
import numpy as np

__author__ = "Trey Gower"
__version__ = "0.1"

"""
Intended use is to apply singular value decomposition to solve for a linear system of equations.
Factoring one matrix into three A = U*(Sigma)*(V^T)
"""


def Enter_matrix():
    """
    Takes user input to create a matrix A

    Args: None

    Returns: user inputted matrix
    """
    n = input("Enter number of rows: \n")
    m = input("Enter number of columns: \n")
    A = np.zeros([int(n), int(m)], dtype=int)
    # Populate matrix A
    for i in range(int(n)):
        for j in range(int(m)):
            val = input("Enter A" + str(i + 1) + str(j + 1) + " value: ")
            A[i, j] = int(val)
    return A


def Solve_V_U(A):
    """
    Takes matrix A and calulates the orthonormal matrix V and U

    Args: A matrix titled (A)

    Returns: a list containing a matrix V (nxn) and a matrix U (mxm) containing the orthonormal eigenvectors:
    (A^T)*(A) and (A)*(A^T) respectively.
    """
    X = []
    AT = np.transpose(A, axes=None)
    V = np.matmul(AT, A)  # A^T*A matrix
    U = np.matmul(A, AT)  # A*A^T matrix
    X = [V, U]
    return X


def Solve_sigma(V):
    """
    Takes matrix V or U (Both have same eigen values) and calulates the diagonal matix Sigma with roots of
    positive eigen values

    Args: A matrix titled A (nxm)

    Returns: A matrix Sig (diagnial matrix) containing r elements equal to the root of the positive eigen values
    """
    Sigma = np.zeros(np.shape(V))
    eig_val = np.linalg.eigvals(V)
    # Check for positve eigen values
    for i in range(len(eig_val)):
        if eig_val[i] < 0:
            return "Error Non-Positive Eigen Value" + str(eig_val[i])
        else:
            Sigma[i, i] = eig_val[i]
    return Sigma


def main():
    """Main entry point of the app"""
    A = Enter_matrix()
    print("Matrix A: ")
    print(str(A))
    print("")
    X = Solve_V_U(A)
    Sigma = Solve_sigma(X[0])
    print("Matrix V: ")
    print(X[0])
    print("")
    print("Matrix Sigma: ")
    print(Sigma)
    print("")
    print("Matrix U: ")
    print(X[1])


if __name__ == "__main__":
    """This is executed when run from the command line"""
    main()
