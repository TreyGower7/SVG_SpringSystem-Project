import numpy as np
import math
import SingleValueDecomp as SVDAlg


def main():
    """Comparing Svd black box and my algorithm"""
    J = SVDAlg.SVD()
    print(np.linalg.svd(J[5]))
    # deletes Condition number, A inverse, and A matrix
    J.pop()
    J.pop()
    J.pop()

    print(J)


if __name__ == "__main__":
    main()
