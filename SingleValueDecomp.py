import math
import numpy as np

"""
Intended use is to apply singular value decomposition to solve for a linear system of equations.
Factoring one matrix into three A = U*(Sigma)*(V^T)
"""
__author__ = "Trey Gower"
__version__ = "0.1"

def Solve_V(A):
    """
    Takes matrix A and calulates the orthonormal matrix V

    Args: A matrix titled (A)
    
    Returns: A matrix V (nxn) containing the orthonormal eigenvectors: (A^T)*(A)
    """


def Solve_U(A):
    """
    Takes matrix A and calulates the orthonormal matrix V

    Args: A matrix titled A (nxm)
    
    Returns: A matrix U (mxm) containing the orthonormal eigenvectors: (A)*(A^T)
    """


def Solve_Sig(A):
    """
    Takes matrix A and calulates the orthonormal matrix V

    Args: A matrix titled A (nxm)
    
    Returns: A matrix Sig (diagnial matrix) containing r elements equal to the root of the positive eigen values 
    """

def main():
    """ Main entry point of the app """
    print("hello world")


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
