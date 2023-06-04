from util import *
from Graph_P1 import GraphP1
from Graph_PC import GraphPC
from Player import Player

G = nx.DiGraph()
v1 = Player("v1", {"c1","s1"})
v2 = Player("v2", {"c2","s2"})
vBot = Player("v3", {})
v1.set_preferences([{(v1,v2), (v2,v1)}, {(v1,vBot)}, {(v1,v2),(v2,vBot)}])
v2.set_preferences([{(v2,v1), (v1,v2)}, {(v2,vBot)}, {(v2,v1),(v1,vBot)}])
players = [v1, v2, vBot]
G.add_nodes_from(players)

edge_list = [(v1,v2,{"w": "c1"}),(v2,v1,{"w": "c2"}),(v1,vBot,{"w": "s1"}),(v2,vBot,{"w": "s2"})]
G.add_edges_from(edge_list)

graph_p1 = GraphP1(G, get_strategy_profiles(G))
graph_pc = GraphPC(G,get_strategy_profiles(G))
affichage_dyna(graph_pc.graph_dyna)
