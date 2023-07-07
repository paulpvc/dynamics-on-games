from util import *
from Propre.Game.Graph_PC import GraphPC
from Propre.Game.Player import Player

G = nx.DiGraph()
v1 = Player("v1")
v2 = Player("v2")
v3 = Player("v3")
vBot = Player("vB")
v1.set_preferences([{(v1,vBot)}, {(v1,v2), (v2,vBot)}])
v2.set_preferences([{(v2,vBot)}, {(v2, v3),(v3, v1),(v1,vBot)}])
v3.set_preferences([{(v3, vBot)}])
players = [v1, v2, v3, vBot]
G.add_nodes_from(players)

edge_list = [(v1,v2,{"w": "c1"}),(v2,v3,{"w": "c2"}),(v3,v1, {"w":"c3"}),(v1,vBot,{"w": "s1"}),(v2,vBot,{"w": "s2"}),(v3,vBot,{"w": "s3"})]
G.add_edges_from(edge_list)
affichage(G, "main")
#graph_p1 = GraphP1(G, get_strategy_profiles(G))
graph_pc = GraphPC(G,get_strategy_profiles(G))
#graph_bp1 = GraphbP1(G, get_strategy_profiles(G))
#graph_bpc = GraphbPC(G, get_strategy_profiles(G))
affichage_dyna(graph_pc.graph_dyna, "PC")

"""temp = find_dw(G)
if temp:
    print("terminaison équitable de bPC: impossible de savoir car il y a une DW")
else:
    print("terminaison équitable de bPC:", not temp)
"""