from util import *
from Player import Player
from Strategy import Strategy

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
strat2 = Strategy({"s1"})

preferences = {player1: [(strat1, strat2, strat3)],
               player2: [{(player2,player1), (player1,player2)}, {(player2,player3)}, {(player2,player1),(player1,player3)}]}

player1.set_preferences(preferences[player1])

