from math import nan
import matplotlib.pyplot as plt


def draw_degree_to_probability(degrees, n):
    degree_probability = [degrees.count(i) / n for i in range(n)]
    plt.plot(range(n), [x if x != 0.0 else nan for x in degree_probability], 'ro')
    plt.xlim(xmin=min(degrees) - 5, xmax=max(degrees) + 5)
    plt.xlabel('k')
    plt.ylabel('P(k)')
    plt.show()
