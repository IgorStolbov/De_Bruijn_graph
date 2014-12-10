import networkx as nx
import matplotlib as plt

n = 12
m = 2
a = 2

getbit = lambda x, i: (x >> i) & 1

class bitnode:
    value = 0
    def __init__(self, n):
        self.value = n
    def sum(self, t):
        result = self.value ^ t.value
        return bitnode(result)
    def mult(self, t):
        s1 = [int(i) for i in bin(self.value)[2:]]
        s2 = [int(i) for i in bin(t.value)[2:]]
        result = []
        for i, j in enumerate(s1[::-1]):
            if j != 0:
                result.append(0)
        return result

class DBgraph:
    G=nx.MultiGraph()
    def build(self):
        G = self.G
        for i in range(2**n):
            G.add_node(bitnode(i))
        for i in G:
            G.add_edge(i, i.mult(m))
            G.add_edge(i, (i.mult(m)).sum(a))
        return
    def show(self):
        return

def main():
    n = int("1000000", 2)
    print(n)
    print(getbit(n,3))
    return
main()
