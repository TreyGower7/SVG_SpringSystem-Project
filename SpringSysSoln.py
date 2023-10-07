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
        K.append(float(input("Enter Spring constant K" + str(i + 1) + "[N/m]: ")))

    for i in range(num_M):
        M.append(float(input("Enter Mass m" + str(i + 1) + "[kg]: ")))

    # enter boundary conditions
    while int(B_conds) < 1 or int(B_conds) > 3:
        B_conds = input(
            "Enter Boundary conditions (1)Fixed/Fixed (2)Fixed/Free (3)Free/Free: "
        )

    data = [K, M, B_conds]
    return data


def internal_force(K, e):
    # create C matrix
    C = np.zeros(np.shape(K))
    C = np.diag(K)
    # solve w
    w = np.dot(C, e)
    return w


def elongation(u, m):
    # initialize e as an mx1 column vector
    e = np.array(np.zeros((int(m), 1)))
    # create elongation vector from u values
    for i in range(len(u) - 1):
        e[i] = u[i + 1] - u[i]

    return e


def force_balance(M, Kinv, B_conds):
    # calculate force vector
    f = np.array(M) * (9.81)  # [m/s^2]
    if len(Kinv) < len(f) or len(Kinv) > len(f):
        print("Improper Boundary Conditions Set")
        exit()
    u = np.dot(f, Kinv)

    if int(B_conds) == 2:
        # first K row and column is deleted and force for that K set to 0
        u = np.insert(u, 0, 0)
    # Fixed/Fixed case
    if int(B_conds) == 1:
        # first and last K row and column is deleted and force for those K's deleted
        # u = np.insert(u, 0, 0)
        # u = np.append(u, 0, 0)
        u = np.concatenate(([0], u, [0]))
    return u


# creating the stiffness matrix
def create_Kmat(Kvec, Mvec, B_conds):
    if len(Mvec) == len(Kvec) or len(Mvec) < len(Kvec):
        Kvec = np.append(Kvec, Kvec[-1])

    m = int(len(Kvec))
    K = np.zeros((m, m))

    # populate diagnol
    for i in range(m):
        if i == 0 or i == m - 1:
            K[i, i] = Kvec[i]
        else:
            K[i, i] = Kvec[i - 1] + Kvec[i]

    # Populate the off-diagonal elements (negative spring constants)
    for i in range(m - 1):
        K[i, i + 1] = -Kvec[i]
        K[i + 1, i] = -Kvec[i]
    # Free/Free case
    if int(B_conds) == 3:
        # no action necessary for free/free
        K_new = K
    # Fixed/Free case
    if int(B_conds) == 2:
        # first K row and column is deleted
        K_new = K[1:, 1:]
    # Fixed/Fixed case
    if int(B_conds) == 1:
        # first and last K row and column is deleted
        K_new = K[1:, 1:]
        K_new = K_new[:-1, :-1]

    return [K_new, Mvec]


def main():
    """Solve Ku=f"""
    J = input_data()
    B_conds = int(J[2])

    # calculate K stiffness matrix
    K = create_Kmat(J[0], J[1], J[2])
    M = K[1]
    K = K[0]
    # Svd decomposition of K into ???
    SVDvals = SVDSoln.SVD(K)
    # Kinv from SVD
    Kinv = SVDvals[3]
    # Check condition of K
    if SVDvals[4] >= 100:
        print(
            "Condition Number of K: "
            + str(SVDvals[4])
            + " is too high and K is ill-conditioned"
        )
        exit()
    # calculate u vector based on f vector and Kinv matrix
    u = force_balance(M, Kinv, J[2])
    # calculate elongation vector e by back substituting u
    e = elongation(u, len(J[0]))
    # calculate internal force vector w by back substituting e
    w = internal_force(J[0], e)

    print("Condition Number of K: " + str(SVDvals[4]))
    print("")
    print("Singular Values of K: " + str(SVDvals[1]))
    print("")
    print("Eigen Values of K: " + str(np.power(2, SVDvals[1])))

    print("K matrix:")
    print(K)
    print("u vector:")
    print(u)
    print("e vector:")
    print(e)
    print("w vector:")
    print(w)


if __name__ == "__main__":
    main()
