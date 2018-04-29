from random import random
from draw import draw_degree_to_probability

if __name__ == '__main__':
    n = 1000
    edges_list = [[1], [0]]
    for i in range(len(edges_list), n):
        new_vertex = []
        edges_list.append(new_vertex)
        for j in range(len(edges_list) - 1):
            if len(edges_list[j]) / sum(map(len, edges_list)) > random():
                edges_list[j].append(i)
                new_vertex.append(j)
    degrees = [len(x) for x in edges_list]
    draw_degree_to_probability(degrees, n)

