
import numpy as np
import scipy as sp
def generate_game_state(faces,n):
    ring = generate_ring_matrix(faces,n)
    A = np.random.random(len(faces))
    return ring,A

def generate_ring_matrix(faces,n):
    bell = lambda x, m, s: np.exp(-((x-m)/s)**2 / 2)
    adj = generate_adj_matrix(faces,np.max(faces))
    dist = dist_gen(adj, n)/n
    ring_matrix = bell(dist,0.5,0.15)
    ring_matrix = ring_matrix/np.sum(ring_matrix,axis=1)[:,np.newaxis]
    return ring_matrix

def generate_adj_matrix(faces,n):
    size = len(faces)
    adj_matrix = sp.sparse.coo_matrix(([], ([], [])), shape=(size,size),dtype=int)
    for i in range(n):
        coords = np.any(faces==i,axis=1).nonzero()[0]
        coords_len = len(coords)
        row = np.repeat(coords,coords_len-1)
        col = np.delete(np.tile(coords, coords_len), range(0, coords_len ** 2, coords_len+1))
        i_adj =  sp.sparse.coo_array((np.ones(coords_len**2-coords_len),(row, col)),shape = (size,size))
        adj_matrix += i_adj.astype(int)
    return adj_matrix
        

def dist_gen(adj, n):
    """
    input:
        adj: a square CSR adjacency matrix
        n: number of steps we are searching
    output:
        dist_matrix: a distance matrix containing the radius reachable in n steps and the time to get there
    """
    # Compute the shortest path from each node to all other nodes using BFS algorithm
    dist_matrix = sp.sparse.csgraph.dijkstra(adj, limit=n)
    # Replace infinite values with zero to reflect that the distance from a node to itself is zero
    dist_matrix[np.isinf(dist_matrix)] = 0

    return dist_matrix


def gol_update(A,kernel,m,s,frames):
    A = np.clip(A+growth(kernel.dot(A),m,s)/frames,0,1)
    return A


def growth(U,m,s): 
    """
    Computes the growth function for updating the grid using the Game of Life rules.

    Parameters:
    - U (numpy.array): 1D array representing the input for the growth function.
    - m (float): Mean value for the growth function.
    - s (float): Standard deviation value for the growth function.

    Returns:
    - result(numpy.array): 1D array representing the computed growth function.
    """
    bell = lambda x, m, s: np.exp(-((x-m)/s)**2 / 2)
    return bell(U, m, s)*2-1


    
    

