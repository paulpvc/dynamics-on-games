from util import *
from Player import Player
from Strategy import Strategy
from Graph_P1 import GraphP1
from Graph_PC import GraphPC
from Graph_bP1 import GraphbP1
from Graph_bPC import GraphbPC

G = nx.DiGraph()

player1 = Player("v1")
player2 = Player("v2")
player3 = Player("vb")


G.add_node(player1)
G.add_node(player2)
G.add_node(player3)


edge_list = [(player1,player2,{"w": "c1"}),(player2,player1,{"w": "c2"}),(player1,player3,{"w": "s1"}),(player2,player3,{"w": "s2"})]
G.add_edges_from(edge_list)


strat1 = Strategy({"c1", "c2"})
strat3 = Strategy({"c1", "s2"})
strat4 = Strategy({"s1", "c2"})
strat5 = Strategy({"s2"})
strat2 = Strategy({"s1"})

preferences = {player1: [(strat1, strat2, strat3)],
               player2: [(strat1, strat5, strat4)]}
"""[{(player2,player1), (player1,player2)}, {(player2,player3)}, {(player2,player1),(player1,player3)}]"""
player1.set_preferences(preferences[player1])
player2.set_preferences(preferences[player2])

graph_p1 = GraphP1(G, get_strategy_profiles(G))
graph_pc = GraphPC(G,get_strategy_profiles(G))
graph_bp1 = GraphbP1(G, get_strategy_profiles(G))
graph_bpc = GraphbPC(G, get_strategy_profiles(G))
lst = [graph_p1, graph_bp1, graph_pc, graph_bpc]
label = ["P1", "bP1", "PC", "bPC"]
for i in range(len(lst)):
    affichage_dyna(lst[i].graph_dyna, label[i])

