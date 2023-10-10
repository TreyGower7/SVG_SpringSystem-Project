import numpy as np
import math
import SingleValueDecomp as SVDAlg


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


def main():
    """Comparing Svd black box and my algorithm"""
    A = Enter_matrix()
    J = SVDAlg.SVD(A)
    Blackbox = np.linalg.svd(A)

    # deletes Condition number, A inverse, and A matrix
    J.pop()
    J.pop()
    J.pop()

    print("My Routine (U):")
    print(J[0])
    print("Blackbox (U):")
    print(Blackbox[0])
    print("My Routine (Sigma):")
    print(J[1])
    print("Blackbox (Sigma):")
    print(Blackbox[1])
    print("My Routine (V):")
    print(J[2])
    print("Blackbox (V):")
    print(Blackbox[2])


if __name__ == "__main__":
    main()
