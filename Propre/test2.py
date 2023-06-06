from util import *
from Player import Player


G = nx.DiGraph()

player1 = Player("v1")
player2 = Player("v2")
player3 = Player("vb")


G.add_node(player1)
G.add_node(player2)
G.add_node(player3)


edge_list = [(player1,player2,{"w": "c1"}),(player2,player1,{"w": "c2"}),(player1,player3,{"w": "s1"}),(player2,player3,{"w": "s2"})]
G.add_edges_from(edge_list)

preferences = {player1: [({"c1", "c2"}, {"s1"}, {"c1", "s2"})],
               player2: [{(player2,player1), (player1,player2)}, {(player2,player3)}, {(player2,player1),(player1,player3)}]}

player1.set_preferences(preferences[player1])

