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


def Solve_U(eig_val, eig_vec):
    """
    calulates the orthonormal matrix U

    Args: eig_val: eigen values, eig_vec: eigen vectors

    Returns: the U matrix
    """
    # Sort eigen vectors and value and solve U
    sorted_indices = np.argsort(eig_val)[::-1]
    eigenvalues = eig_val[sorted_indices]
    eigenvectors = eig_vec[:, sorted_indices]
    U = eigenvectors / np.linalg.norm(eigenvectors, axis=0)
    return U


def Solve_Sigma(W, eig_val):
    """
    calulates the diagonal matrix sigma

    Args: W: A*A^T, eig_val: eigen values

    Returns: A matrix Sig (diagnial matrix) containing r elements equal to the root of the positive eigen values
    """
    Sigma = np.zeros(np.shape(W))
    # Check for positve eigen values and solve sigma
    for i in range(len(eig_val)):
        if eig_val[i] <= 0:
            return "Error Non-Positive or Zero Eigen Value" + str(eig_val[i])
        else:
            Sigma[i, i] = math.sqrt(eig_val[i])
    return Sigma


def Solve_V(A, eig_val, U):
    """
    calulates the orthonormal matrix V

    Args: A: nxm matrix, eig_val: eigen values, U: orthonormal U matrix

    Returns: the V matrix
    """
    U_1 = U[:, 0]
    U_2 = U[:, 1]
    return U_1


def Solve_Condition(eig_val):
    # condition number is ||A||_2 * ||A^-1||_2 or |Lamda_max|/|Lamda_min|
    CondNum = np.max(eig_val) / np.min(eig_val)
    return CondNum


def Solve_Ainv(Sigma):
    Sigmainv = np.zeros(np.shape(Sigma))

    # inverse of matrix Sigma is just the reciprical of the diagonal values in sigma
    for i in range(len(Sigma)):
        Sigmainv[i, i] = 1 / Sigma[i, i]


def SVD():
    """
    Returns a dictionary of all SVD matrices, condition number and the inverse given by A^-1= V*Sigma^{-1}*U^T
    """
    A = Enter_matrix()
    # A^T*A matrix
    AT = np.transpose(A, axes=None)
    W = np.matmul(AT, A)
    # Eigen values and vectors
    eig_val, eig_vec = np.linalg.eig(W)

    # Solve matrices of SVD
    U = Solve_U(eig_val, eig_vec)
    Sigma = Solve_Sigma(W, eig_val)
    V = Solve_V(W, eig_val, eig_vec)
    print(V)
    # Solve Ainv and Condition number of A
    # Ainv = Solve_Ainv(Sigma)
    CondNum = Solve_Condition(eig_val)

    soln = [U, Sigma, V, CondNum]
    return soln
