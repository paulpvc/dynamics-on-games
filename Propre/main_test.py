from util import *
from Graph_P1 import GraphP1
from Player import Player

G = nx.DiGraph()
player1 = Player("v1", {"c1","s1"})
player2 = Player("v2", {"c2","s2"})
player3= Player("v3", {})
player1.set_preferences([{(player1,player2), (player2,player1)}, {(player1,player3)}, {(player1,player2),(player2,player3)}])
player2.set_preferences([{(player2,player1), (player1,player2)}, {(player2,player3)}, {(player2,player1),(player1,player3)}])
players = [player1, player2, player3]
G.add_nodes_from(players)

edge_list = [(player1,player2,{"w": "c1"}),(player2,player1,{"w": "c2"}),(player1,player3,{"w": "s1"}),(player2,player3,{"w": "s2"})]
G.add_edges_from(edge_list)

affichage(G)
print(get_strategy_profiles(G))


graph_p1 = GraphP1(G, get_strategy_profiles(G))
affichage_dyna(graph_p1.graph_dyna)
