import numpy as np
import SingleValueDecomp as SVDSoln


def input_data():
    # initialize variables
    K = []
    M = []
    B_conds = 0

    print(
        "Input so that the num of springs = num of masses or num of spring+1 = num of masses"
    )
    num_K = int(input("How many springs: "))
    num_M = int(input("How many masses: "))

    # Check to ensure the system is solvable with at most one more mass than spring or vice versa
    if num_K != num_M:
        if num_K > num_M + 1 or num_M > num_K + 1:
            raise Exception("Two little or too many springs entered")
    # Input spring constants and mass values
    for i in range(num_K):
        K.append(int(input("Enter Spring constant K" + str(i + 1) + "[N/m]: ")))
        # ensuring only #M=#K or #M=#K+1
        if i < num_M:
            M.append(int(input("Enter Mass m" + str(i + 1) + "[kg]: ")))

    # enter boundary conditions
    while int(B_conds) < 1 or int(B_conds) > 3:
        B_conds = input(
            "Enter Boundary conditions (1)Fixed/Fixed (2)Fixed/Free (3)Free/Free: "
        )

    data = [K, M, B_conds]
    return data


def elongation(u, m):
    # initialize e as an mx1 column vector
    e = np.array(np.zeros((int(m), 1)))
    print(e)
    # create elongation vector from u values and based on boundary conditions
    for i in range(1, len(u)):
        e[i - 1] = u[i] - u[i - 1]

    return e


# def internal_force(K, u):

#  return C


def force_balance(M, Kinv, B_conds):
    # calculate force vector
    f = np.array(M) * (9.81)  # [m/s^2]
    print(f)
    u = np.dot(f, Kinv)

    return u


# creating the stiffness matrix
def create_Kmat(Kvec, Mvec):
    m = int(len(Kvec))
    K = np.zeros(m, m)
    for i in range(len(K)):
        for j in range(len(K)):
            # populate stiffness below main diagonal
            if j == i + 1:
                K[i, j] = -Kvec[i]
            # populate stiffness to the right of main diagonal
            if i == j + 1:
                K[i, j] = -Kvec[j]
            # populate main diagonal
            if i == j:
                if j == 0 or j == len(K):
                    K[i, j] = Kvec[i]
                else:
                    K[i, j] = num_k[i - 1] + num[i]
        # Free/Free case
    if B_conds == 3:
        # no action necessary for free/free
        return K
    # Fixed/Free case
    if B_conds == 2:
        # first K row and column is deleted and force for that K deleted
        
    # Fixed/Fixed case
    else:
        # first K row and column is deleted and force for that K deleted
        u[0] = 0
        u[-1] = 0
    return K


def main():
    """Solve Ku=f"""
    J = input_data()
    B_conds = int(J[2])

    # calculate K stiffness matrix
    K = create_Kmat(J[0], J[1])
    # Svd decomposition of K into ???
    SVDvals = SVDSoln.SVD(K)
    # Kinv from SVD
    Kinv = SVDvals[3]
    # calculate u vector based on f vector and Kinv matrix
    u = force_balance(J[1], Kinv, B_conds)
    # calculate elongation vector e by back substituting u
    e = elongation(u, len(J[0]))
    # calculate internal force vector w by back substituting e
    # w = internal_force(J[0],u)


if __name__ == "__main__":
    main()
