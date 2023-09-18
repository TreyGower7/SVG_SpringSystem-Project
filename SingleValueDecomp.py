import numpy as np
import math

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


def Solve_sigma_condnum(V):
    """
    Takes matrix V or U (Both have same eigen values) and calulates the diagonal matix Sigma with roots of
    positive eigen values. Also calculates Condtiion Number.

    Args: A matrix titled V (nxm)

    Returns: A matrix Sig (diagnial matrix) containing r elements equal to the root of the positive eigen values
    """
    Sigma = np.zeros(np.shape(V))
    eig_val = np.linalg.eigvals(V)
    # Check for positve eigen values
    for i in range(len(eig_val)):
        if eig_val[i] <= 0:
            return "Error Non-Positive or Zero Eigen Value" + str(eig_val[i])
        else:
            Sigma[i, i] = math.sqrt(eig_val[i])
    # condition number is ||A||_2 * ||A^-1||_2 or |Lamda_max|/|Lamda_min|
    CondNum = np.max(eig_val) / np.min(eig_val)
    return [Sigma, CondNum]


def SVD():
    """
    Returns all SVD matrices, condition number and the inverse given by A^-1= V*Sigma^{-1}*U^T
    """
    A = Enter_matrix()
    X = Solve_V_U(A)
    U = X[0]
    V = X[1]
    L = Solve_sigma_condnum(V)
    Sigma = L[0]
    Sigmainv = np.zeros(np.shape(Sigma))
    CondNum = L[1]
    # inverse of matrix Sigma is just the reciprical of the diagonal values in sigma
    for i in range(len(Sigma)):
        Sigmainv[i, i] = 1 / Sigma[i, i]
    soln = [U, Sigma, V, CondNum]
    return soln


def main():
    """Main entry point of the app"""
    J = SVD()

    print(J[1])
    print(J[2])
    print(J[3])


if __name__ == "__main__":
    """This is executed when run from the command line"""
    main()
