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

preferences_v1 = [[(1,2), (2,1)], [(1,3)], [(1,2),(2,3)]]
preferences_v2 = [[(2,1), (1,2)], [(2,3)], [(2,1),(1,3)]]