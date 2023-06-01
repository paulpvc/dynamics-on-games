import networkx as nx
import my_networkx as my_nx
import matplotlib.pyplot as plt
from Pile import Pile
from graphs import *
from util import *

G = nx.DiGraph()

edge_list =[(1,2,{"w": "c1"}),(2,3,{"w": "c2"}), (3,1,{"w": "c3"}), (1,4,{"w": "s1"}), (2,4,{"w": "s2"}), (3,4,{"w": "s3"})]
G.add_edges_from(edge_list)

affichage(G, "MAIN")

nodes = list(G.nodes())
nodes.sort(key=lambda x: len(list(G.neighbors(x))))
nodes = nodes[1:]
chemins_dyna = const_chemins(G, nodes, 0)
dyna_pc = const_dyna_graph_PC(preferences, chemins_dyna)

