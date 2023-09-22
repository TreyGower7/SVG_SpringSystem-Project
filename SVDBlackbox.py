import numpy as np
import math


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
    """Main entry point of the app"""
    A = Enter_matrix()
    print(np.linalg.svd(A))


if __name__ == "__main__":
    main()
