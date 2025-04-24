"""
Take our X_i, create all pairs of their values (len (X_i) choose 2)
calculate the difference of those pairs through our modular equation
add it to our new set
take the union of all X_i
pop out values from the union of sets, constructing copies of our sets (check if its a copy)
if we have lambda copies, valid SDS
Methodology:
I initially tried to make it so I was creating lambda arrays and seeing if we had lambda copies but that was
horribly inneficient, I instead changed my appraoch to checking if I have lambda copies of each element, which is sufficient
to prove I have enough elements to create lambda sets with all unique elements.
"""



from itertools import combinations

def is_sds(v, lam, X_sets):
    """
    Determine whether the given collection of sets forms a valid SDS (t-{v; k1,...,kt; λ} supplementary difference sets).
    
    Parameters:
    - v (int): The modular base for our ring Z_v
    - lam (int): The parameter λ, representing how many final copies we should have
    - X_sets (list of sets of int): A list of t subsets (S1, S2, ..., St) 
    
    Returns:
    - bool: True if the sets in X_sets form an SDS with parameters (v; k1,...,kt; λ), False otherwise.
    """
    # check the size of each subset
    k_values = [len(X) for X in X_sets]
    
    #verify the LHS = RHS of our equation first
    left_side = lam * (v - 1)
    right_side = sum(k * (k - 1) for k in k_values)
    if left_side != right_side:
        return False
    
    # A frequency counter for our differences
    diff_count = [0] * v
    
    # Compute all directed differences within each subset
    for X in X_sets:
        for x in X:
            for y in X:
                if x != y:  # only consider pairs of distinct elements
                    d = (x - y) % v  # directed difference mod v
                    if d != 0:
                        diff_count[d] += 1
    #this operation had to be done in O(n^3), O(n) with wasteful spacial management
    
    # check if we have lambda copies of each element in our main set
    for d in range(1, v):
        if diff_count[d] != lam:
            return False
    
    # If all counts match λ, the sets form a valid SDS
    return True
