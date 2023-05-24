import networkx as nx
import my_networkx as my_nx
import matplotlib.pyplot as plt
from Pile import Pile

G = nx.DiGraph()

G.add_node(1)
G.add_node(2)
G.add_node(3)

edge_list = [(1,2,{"w": "c1"}),(2,1,{"w": "c2"}),(1,3,{"w": "s1"}),(2,3,{"w": "s2"})]
G.add_edges_from(edge_list)

preferences = [[{(1,2), (2,1)}, {(1,3)}, {(1,2),(2,3)}],
               [{(2,1), (1,2)}, {(2,3)}, {(2,1),(1,3)}]]

def affichage(G):
    pos = nx.spring_layout(G, seed=5)
    fig, ax = plt.subplots()
    nx.draw_networkx_nodes(G, pos, ax=ax)
    nx.draw_networkx_labels(G, pos, ax=ax)

    curved_edges = [edge for edge in G.edges()]
    nx.draw_networkx_edges(G, pos, edgelist=curved_edges, connectionstyle='arc3, rad=0.25')
    edge_weights = nx.get_edge_attributes(G, 'w')
    curved_edge_labels = {edge: edge_weights[edge] for edge in curved_edges}
    my_nx.my_draw_networkx_edge_labels(G, pos, ax=ax, edge_labels=curved_edge_labels, rotate=False, rad=0.25)
    plt.show()


affichage(G)

"""dyna_P1 = nx.DiGraph()
all_neighbors = [G.neighbors(n) for n in G.nodes()]
for i in range(len(all_neighbors)):
    neighbors = all_neighbors[i]
"""
nodes = list(G.nodes())
nodes.sort(key=lambda x: len(list(G.neighbors(x))))
nodes = nodes[1:]
print(nodes)

"""def const_chemins_old(G: nx.DiGraph, nodes, i):
    if i < len(nodes):
        res = []
        for n in G.neighbors(nodes[i]):
            temp = const_chemins(G, nodes, i+1)
            if not temp:
                res.append([(nodes[i],n)])
            else:
                for ch in temp:
                    res.append([(nodes[i],n)] + ch)

        return res
    return []"""


def const_chemins(G: nx.DiGraph, nodes, i):
    if i < len(nodes):
        res = []
        for n in G.neighbors(nodes[i]):
            temp = const_chemins(G, nodes, i+1)
            if not temp:
                res.append({(nodes[i], n)})
            else:
                for ch in temp:
                    ch.add((nodes[i], n))
                    res.append(ch)

        return res
    return []


chemins_dyna = const_chemins(G, nodes, 0)
print(chemins_dyna)

def gain(preferences: list, strategy: set, i: int):
    for j in range(len(preferences[i])):
        pref = preferences[i][j]
        if pref.issubset(strategy):
            return j
    return 0

for i in range(len(preferences)):
    print(f'gains joueur {i+1}:')
    for ch in chemins_dyna:
        print(ch, gain(preferences, ch, i))
