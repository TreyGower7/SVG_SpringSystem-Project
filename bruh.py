import numpy as np

# Create a sample matrix
A = np.array([[3, 2], [3, 4]])

# Step 1: Perform SVD on the original matrix
U, S, Vt = np.linalg.svd(A)

# Step 2: Compute the inverse of the singular values
S_inv = np.diag(1.0 / S)

# Step 3: Reconstruct the inverse of the original matrix
A_inv = Vt.T @ S_inv @ U.T

print("Original Matrix (A):")
print(S)
print("\nInverse Matrix (A_inv):")
print(A_inv)
