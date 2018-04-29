from random import random
from draw import draw_degree_to_probability

if __name__ == '__main__':
    n = 1000
    p = 0.4
    edge_matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i, n):
            if random() < p:
                edge_matrix[i][j] = 1
                edge_matrix[j][i] = 1
    degrees = [sum(edge_row) for edge_row in edge_matrix]
    draw_degree_to_probability(degrees, n)
