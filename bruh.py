import numpy as np

# Define the stiffness matrix (K)
k = 1000  # Stiffness coefficient of the spring
K = np.array([[k, -k], [-k, k]])

# Define boundary conditions
# Node 1 is fixed (u1 = 0), and node 2 is free
fixed_nodes = [1]  # List of fixed nodes (node numbering starts from 1)

# Apply fixed boundary conditions to the stiffness matrix
for node in fixed_nodes:
    K[node - 1, :] = 0  # Set the entire row to 0
    K[:, node - 1] = 0  # Set the entire column to 0
    K[node - 1, node - 1] = 1  # Set the diagonal element to 1

# Now, K represents the modified stiffness matrix with fixed-free boundary conditions
print("Modified Stiffness Matrix (with fixed-free boundary conditions):")
print(K)
