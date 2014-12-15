import networkx as nx
from numpy import *
from networkx_viewer import Viewer

n = 8
m = 2
a = 2

def mult(a, b):
    result = 0
    carry = 0
    for counter in range(n):
        if b & 1:
            result ^= a
        carry = a & (2**(n-1))  # detect if x^n term is about to be generated
        a <<= 1
        if carry:
            a ^= 0x1B #replace x^20 with x^3 + 1
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
#    nx.draw(G)
#    nx.draw(G,pos=nx.spectral_layout(G), nodecolor='r',edge_color='b')
    app = Viewer(G)
    app.mainloop()
    return

main()
