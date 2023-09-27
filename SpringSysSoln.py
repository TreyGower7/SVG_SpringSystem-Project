import numpy as np
import SingleValueDecomp as svdsoln


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


# Creating a difference matrix
def Make_A(B_conds, K):
    # Free/Free case#
    if B_conds == 3:
        u = np.zeros(np.shape(K))
        print(u)
        for i in range(len(K)):
            u[i] = sp.symbols("u" + str(i))
    # Fixed/Free case
    if B_conds == 2:
        u = np.zeros(np.shape(K - 1))

    # Fixed/Fixed case
    else:
        u = np.zeros(np.shape(K - 2))
    return u


# def elongation():


def internal_force(K):
    # Make our Spring constant diagonal matrix
    C = np.array(K)
    C = diag(C)
    return C


def force_balance(M, K):
    # calculate force vector
    f = np.array(M) * (9.81)  # [m/s^2]

    u = np.dot(f, Kinv)

    return u


# creating the stifness matrix
def create_K(C):
    K = np.zeros(np.shape(C))

    for i in range(len(K)):
        for j in range(len(K)):
            if j == i + 1 or i == j + 1:
                K[i, j] = -C[i, i]
            if i == j:
                if j == 1 or j == len(K):
                    K[i, j] = C[i, i]
                else:
                    K[i, j] = C[i - 1, i - 1] + C[i, i]
    return K


def main():
    """Comparing Svd black box and my algorithm"""
    J = input_data()

    #    Make our Spring constant diagonal matrix
    C = np.array(J[0])
    C = np.diag(C)

    # calculate A matrix based on displacement vector u
    # A = force_balance(J[1], J[0])
    K = create_K(C)
    # calculate internal force vector w to substitute
    # w = internal_force(J[0])
    print(K)


if __name__ == "__main__":
    main()
