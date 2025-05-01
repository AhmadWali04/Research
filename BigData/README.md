# Synopsis

There is a higher level and lower level understanding of SDS attached in the two PDF's. Currently I have code which helps to test if a set is a SDS, and am working on implementing a self sorting graph algorithm to find new families of SDS. Here is an example of the self sorting graph. Its implimentation is currently being developed through Maple and is in testing to find faults and improvements with Dr.Ilias S Kotserias

 Lets say that I create a graph of 2 types of nodes, black and blue. All black nodes
 represent values {0, ..., v-1} where they each require λ edges from blue nodes to prove
 that they have sufficient quantity to produce a SDS. A blue node would be the pair of
 values {x,y} from X_i that produce a black node. Each blue node will link to 2 black nodes
 (one for "x - y mod v" and the other for "y - x mod v"). The graph can then try to
 rebalance itself by looking at which black nodes have >λ edges, and which have <λ edges.
 In the case where we have a node with >λ edges, we try and find a new (x,y) pair from X_i.
 To do this we first check what the other node it connects to is, and find a new pairwise
 operator that links to both the other node (if that node has the correct # of edges), and
 a node with <λ edges (if one exists).
