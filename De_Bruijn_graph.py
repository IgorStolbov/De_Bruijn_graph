import networkx as nx
from numpy import *
import matplotlib.pyplot as plt
from random import randint
import pygraphviz

NUMBER_OF_NEIGHBOURS = 2
NUMBER_OF_ITERATIONS = 50

n = 12
m = 2
a = 2

def game_of_life(G_original):
    print 'game of life'
    G = G_original.copy()
    is_alive = []
    for i in range(0, 2 ** n):
        is_alive.append(True)
    anybody_is_alive = True

    # nx.draw_networkx(G, edgelist=[])
    pos=nx.graphviz_layout(G)
    nx.draw_networkx_nodes(G, pos, node_size=80)
    plt.show()
    while anybody_is_alive:
        # kill or raise from dead
        alives = []
        for v, nbrdict in G.adjacency_iter():
            number_of_neighbours = 0
            for neighbour in nbrdict:
                if (is_alive[neighbour]):
                    number_of_neighbours += 1
            if (number_of_neighbours == NUMBER_OF_NEIGHBOURS):
                is_alive[v] = True
                alives.append(v)
            else:
                is_alive[v] = False

        # check if anybody is alive
        i = 0
        while is_alive[i] == False and i < len(is_alive):
            i += 1
        if i == len(is_alive):
            anybody_is_alive = False
        else:
            # print alives
            nx.draw_networkx_nodes(G, pos, nodelist=alives, node_size=80)
            # nx.draw_networkx(G, edgelist=[], nodelist=alives)
            plt.show()

def diffusion(G_original):
    print 'diffusion'
    G = G_original.copy()

    # here we distrube 0.5 between n vertexes out of 2 ** n
    # and 0.5 between the rest
    weights = []
    for i in range(0, 2 ** n):
        weights.append(1.0 / (2 ** n - n))

    for i in range(0, n):
        v = randint(0, 2 ** n - 1)
        while (weights[v] != 1.0 / (2 ** n - n)):
            v = randint(0, 2 ** n - 1)
        weights[v] = 0.0

    pos=nx.graphviz_layout(G)
    nx.draw_networkx_nodes(G, pos, node_size=80, node_color=weights, cmap=plt.cm.Reds_r)
    plt.show()

    iter = 0
    while iter < NUMBER_OF_ITERATIONS:
        for v, nbrdict in G.adjacency_iter():
            counter = 1
            weight = weights[v]
            for neighbour in nbrdict:
                # print type(neighbour)
                weight += weights[neighbour]
                counter += 1
            weights[v] = weight / counter
        iter += 1

        # drawing
        nx.draw_networkx_nodes(G, pos, node_size=80, node_color=weights, cmap=plt.cm.Reds_r)
        plt.show()


def mult(a, b):
    result = 0
    carry = 0
    for counter in range(n):
        if b & 1:
            result ^= a
        carry = a & (2**(n-1))  # detect if x^n term is about to be generated
        a <<= 1
        if carry:
            a ^= 0x53 #0x1B #replace x^20 with x^3 + 1 # or 3
        b >>= 1
    start = 2
    size = len(bin(result))
    if size-2 > n:
        start += size-2-n
    result = int((bin(result))[start:], 2)
    return result

def main():
    G=nx.MultiGraph()
    for i in range(2**n):
        G.add_node(i)
    for i in G:
        b = mult(i, m)
        G.add_edge(i, b)
        G.add_edge(i, a^b)
    print 'graph was built'

    diffusion(G)
    game_of_life(G)
    

    return

main()
