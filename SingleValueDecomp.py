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
    A = np.zeros([int(n), int(m)], dtype=float)
    # Populate matrix A
    for i in range(int(n)):
        for j in range(int(m)):
            val = input("Enter A" + str(i + 1) + str(j + 1) + " value: ")
            A[i, j] = float(val)
    return A


def Check_eig(eig_val):
    """Checks to see if eigen value are positive"""
    for i in range(len(eig_val)):
        if eig_val[i] > 0:
            continue
        else:
            raise Exception("Error Zero or Non-Positive Eigen value")
    return 1


def Solve_Condition(A, Ainverse):
    # condition number is ||A||_2 * ||A^-1||_2
    CondNum = np.linalg.norm(A, 2) * np.linalg.norm(Ainverse, 2)
    return CondNum


def SVD(A):
    """
    Returns a dictionary of all SVD matrices, condition number and the inverse given by A^-1= V*Sigma^{-1}*U^T
    """
    if A is None:
        A = Enter_matrix()

    # Compute A^T * A and A * A^T
    ATA = np.dot(A.T, A)
    AAT = np.dot(A, A.T)

    # Compute the eigenvalues and eigenvectors of ATA and AAT
    eigenvalues_ATA, eigenvectors_ATA = np.linalg.eig(ATA)
    eigenvalues_AAT, eigenvectors_AAT = np.linalg.eig(AAT)

    # Check for all positive eigen values
    Check_eig(eigenvalues_AAT)

    # Compute the singular values and the left and right singular vectors
    # Singular values are the square roots of the eigenvalues
    singular_values = np.sqrt(eigenvalues_ATA)

    # Sort the singular values and corresponding singular vectors in descending order
    sorted_indices = np.argsort(singular_values)[::-1]
    singular_values = singular_values[sorted_indices]
    U = eigenvectors_AAT[:, sorted_indices]
    Sigma = singular_values
    Vt = eigenvectors_ATA[:, sorted_indices]

    # Solve Ainv and Condition number of A
    Sigma_inv = np.diag(1 / singular_values)
    Ainverse = Vt @ Sigma_inv @ U.T
    CondNum = Solve_Condition(A, Ainverse)

    # Construct the V matrix by taking the transpose of Vt
    V = Vt.T

    soln = [U, Sigma, V, Ainverse, CondNum, A]
    return soln
