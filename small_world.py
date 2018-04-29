from random import random, choice
from draw import draw_degree_to_probability

if __name__ == '__main__':
    n = 1000
    rewire_p = 0.3
    started_degree = 100
    edge_matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(-int(started_degree / 2), int(started_degree / 2)):
            edge_matrix[i][(i + j + 1) % n] = 1
    for i in range(n):
        for j in range(n):
            if edge_matrix[i][j] == 1 and random() > rewire_p:
                new_j = choice(list(set(range(n)) - set(edge_matrix[i]) - {i}))
                edge_matrix[i][j] = 0
                edge_matrix[j][i] = 0
                edge_matrix[i][new_j] = 1
                edge_matrix[new_j][i] = 1
    degrees = [sum(edge_row) for edge_row in edge_matrix]
    draw_degree_to_probability(degrees, n)
