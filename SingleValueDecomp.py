import math
import numpy as np

__author__ = "Trey Gower"
__version__ = "0.1"

"""
Intended use is to apply singular value decomposition to solve for a linear system of equations.
Factoring one matrix into three A = U*(Sigma)*(V^T)
"""


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


def Solve_Sig(A):
    """
    Takes matrix A and calulates the orthonormal matrix V

    Args: A matrix titled A (nxm)

    Returns: A matrix Sig (diagnial matrix) containing r elements equal to the root of the positive eigen values
    """


def main():
    """Main entry point of the app"""
    A = np.array([[2.0, 4.0], [3.0, 1.0]])
    print(A)
    print("")
    X = Solve_V_U(A)
    print(X[1])
    print("")
    print(X[2])


if __name__ == "__main__":
    """This is executed when run from the command line"""
    main()
