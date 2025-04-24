from SDS import is_sds

v = 19
lam = 8

# Define the collection of t sets (S1, S2, S3 in this case)

#Good Example: (19;9,7,6;8)
"""
v = 19
lam = 8
X1 = {0, 1, 2, 3, 5, 7, 12, 13, 16}
X2 = {0, 1, 2, 4, 5, 10, 13}
X3 = {0, 1, 4, 6, 8, 13}
X_sets = [X1, X2, X3]
"""
#Bad Example (15;8,6,5;7)
v = 19
lam = 8
X1 = {0, 1, 2, 3, 5, 7, 13, 16}
X2 = {0, 1, 2, 5, 10, 13}
X3 = {0, 1, 4, 8, 13}
X_sets = [X1, X2, X3]

# Display the input parameters and sets
print(f"Testing SDS for v={v}, λ={lam} with sets:")
print(f"X1 = {X1}")
print(f"X2 = {X2}")
print(f"X3 = {X3}")

# Perform the SDS validation
if is_sds(v, lam, X_sets):
    k_list = [len(X) for X in X_sets]
    t = len(X_sets)
    print(f"Valid SDS :)")
else:
    print("Not valid SDS :(")
