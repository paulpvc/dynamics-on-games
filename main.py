import itertools

import networkx as nx

from graphs import *
from util import *
from itertools import product


"""def get_strategy_profiles(graph: nx.DiGraph):

    players_actions = {}
    for node in list(graph.nodes):
        if graph.out_degree[node] > 0:
            players_actions[node] = list(graph.edges([node]))
    strategy_profiles = [set(strategy_profile) for strategy_profile in (product(*players_actions.values()))]
    return strategy_profiles

G = nx.DiGraph()

edge_list =[(1,2,{"w": "c1"}),(2,3,{"w": "c2"}), (3,1,{"w": "c3"}), (1,4,{"w": "s1"}), (2,4,{"w": "s2"}), (3,4,{"w": "s3"})]
preferences = {1: [{(1,4)}, {(1,2),(2,4)}],
               2: [{(2,4)}, {(2,3),(3,1), (1,4)}],
               3: [{(3,4)}]}
G.add_edges_from(edge_list)

affichage(G, "MAIN")

nodes = list(G.nodes())
nodes.sort(key=lambda x: len(list(G.neighbors(x))))
nodes = nodes[1:]
chemins_dyna = get_strategy_profiles(G)
c = const_chemins(G, nodes, 0)
print(chemins_dyna)
print(c)
dyna_P1 = const_dyna_graph_P1(preferences, c, G)
dyna_pc = const_dyna_graph_PC(preferences, c, G)
affichage_dyna(dyna_pc, "MAINPC")
affichage_dyna(dyna_P1, "MAINP1")"""

lst = list(map(lambda x: "".join(x), list(itertools.product(["c1", "s1"], ["c2", "c6"], ["c3", "s2"], ["c4", "c7"], ["c5", "s3", "c8"]))))
d = nx.DiGraph()
d.add_nodes_from(lst)
affichage(d)

