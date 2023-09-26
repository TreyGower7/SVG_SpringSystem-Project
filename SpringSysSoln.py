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
        if i <= num_M:
            M.append(int(input("Enter Mass m" + str(i + 1) + "[kg]: ")))

    # enter boundary conditions
    while int(B_conds) < 1 or int(B_conds) > 3:
        B_conds = input(
            "Enter Boundary conditions (1)Fixed/Fixed (2)Fixed/Free (3)Free/Free: "
        )

    # List of dict list
    data = [K, M, B_conds]
    return data


# def elongation():

# def internal_force():

# def force_balance():


def main():
    """Comparing Svd black box and my algorithm"""
    J = input_data()
    C = np.zeros(np.shape(len(J[0])))
    # for i in range(J['K'].size())
    # C = np.diag()
    print(C)


if __name__ == "__main__":
    main()
