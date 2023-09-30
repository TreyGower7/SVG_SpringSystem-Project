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

    # Check to ensure the system is solvable
    if num_K != num_M:
        if num_K != num_M + 1:
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


# def elongation():


def internal_force(K, u):
    # Make our Spring constant diagonal matrix
    C = np.array(K)
    C = diag(C)
    return C


def force_balance(M, Kinv, B_conds):
    # calculate force vector
    f = np.array(M) * (9.81)  # [m/s^2]

    # Now to adjust u for boundary conditions
    # Fixed/Fixed case
    if B_conds != 2 or B_conds != 3:
        # last and first u are 0
        u = np.array([[0, 0]])
    # Fixed/Free case
    if B_conds != 3 or B_conds != 1:
        # first u is 0
        u = np.array([[0]])

    u_new = np.dot(f, Kinv)
    u_actual = np.insert(u, 1, u_new)

    return u_actual


# creating the stiffness matrix
def create_Kmat(C):
    K = np.zeros(np.shape(C))

    for i in range(len(K)):
        for j in range(len(K)):
            # populate stiffness below main diagonal
            if j == i + 1:
                K[i, j] = -C[i, i]
            # populate stiffness to the right of main diagonal
            if i == j + 1:
                K[i, j] = -C[j, j]
            # populate main diagonal
            if i == j:
                if j == 0 or j == len(K):
                    K[i, j] = C[i, i]
                else:
                    K[i, j] = C[i - 1, i - 1] + C[i, i]
    return K


def main():
    """Solve Ku=f"""
    J = input_data()

    C = np.array(J[0])
    C = np.diag(C)
    # calculate K stiffness matrix
    K = create_Kmat(C)
    # Svd decomposition of K into ???
    SVDvals = SVDSoln.SVD(K)
    Kinv = SVDvals[3]
    # calculate u vector based on f vector and K matrix
    u = force_balance(J[1], Kinv, J[2])
    # calculate internal force vector w
    # w = internal_force(J[0],u)

    print(u)


if __name__ == "__main__":
    main()
