from util import *
from Player import Player
from Strategy import Strategy
from Graph_P1 import GraphP1
from Graph_PC import GraphPC
from Graph_bP1 import GraphbP1
from Graph_bPC import GraphbPC


player1 = Player("v1")
player2 = Player("v2")
playerB = Player("vb")
lst = [player1, player2, playerB]





def test1(lst):
    edge_list = [(player1, player2, {"w": "c1"}), (player2, player1, {"w": "c2"}), (player1, playerB, {"w": "s1"}),
                 (player2, playerB, {"w": "s2"})]

    G = get_graph(lst, edge_list)
    affichage(G, "main")

    strat1 = Strategy({"c1", "c2"})
    strat3 = Strategy({"c1", "s2"})
    strat4 = Strategy({"s1", "c2"})
    strat5 = Strategy({"s2"})
    strat2 = Strategy({"s1"})

    preferences = {player1: [(strat1, strat2, strat3)],
                   player2: [(strat1, strat5, strat4)]}
    """[{(player2,player1), (player1,player2)}, {(player2,playerB)}, {(player2,player1),(player1,playerB)}]"""
    player1.set_preferences(preferences[player1])
    player2.set_preferences(preferences[player2])

    graph_p1 = GraphP1(G, get_strategy_profiles(G))
    graph_pc = GraphPC(G, get_strategy_profiles(G))
    graph_bp1 = GraphbP1(G, get_strategy_profiles(G))
    graph_bpc = GraphbPC(G, get_strategy_profiles(G))
    lst = [graph_p1, graph_bp1, graph_pc, graph_bpc]
    label = ["P1", "bP1", "PC", "bPC"]
    for i in range(len(lst)):
        affichage_dyna(lst[i].graph_dyna, label[i])
    print(graph_bpc)
    print("terminaison de P1: " + str(graph_p1.does_terminate()))
    print("terminaison de bP1: " + str(graph_bp1.does_terminate()))
    print("terminaison de PC: " + str(graph_pc.does_terminate()))
    print("terminaison de bPC: " + str(graph_bpc.does_terminate()))
    #print("présence d'une SDW: " + str(sdw_1TG(G, graph_pc)))
    """
    affichage_dyna(graph_p1.graph_dyna, "P1")"""
    



def test2(lst):
    player3 = Player("v3")
    lst.append(player3)
    edge_list = [(player1,player2,{"w": "c1"}),(player2,player3,{"w": "c2"}),(player3,player1, {"w":"c3"}),(player1,playerB,{"w": "s1"}),(player2,playerB,{"w": "s2"}),(player3,playerB,{"w": "s3"})]
    G = get_graph(lst, edge_list)
    affichage(G, 'main')

    #strat1 = Strategy({"c1", "c2"})
    strat3 = Strategy({"c1", "s2"})
    strat4 = Strategy({"s1", "c2", "c3"})
    strat5 = Strategy({"s2"})
    strat2 = Strategy({"s1"})
    strat6 = Strategy({"s3"})

    preferences = {player1: [(strat2, strat3)],
                   player2: [(strat5, strat4)],
                   player3: [(strat6,)]}

    player1.set_preferences(preferences[player1])
    player2.set_preferences(preferences[player2])
    player3.set_preferences(preferences[player3])


    nodes_of_dynamique = get_nodes_of_dynamic_graph(G)
    graph_p1 = GraphP1(G, nodes_of_dynamique)
    affichage_dyna(graph_p1.graph_dyna, "p1")
    graph_pc = GraphPC(G, nodes_of_dynamique)
    print("---------------")
    graph_bp1 = GraphbP1(G, nodes_of_dynamique)
    print("---------------")
    graph_bpc = GraphbPC(G, nodes_of_dynamique)
    lst = [graph_p1, graph_bp1, graph_pc, graph_bpc]
    label = ["P1", "bP1", "PC", "bPC"]
    for i in range(len(lst)):
        affichage_dyna(lst[i].graph_dyna, label[i])
    """
    print("terminaison de P1: " + str(graph_p1.does_terminate()))
    print("terminaison de bP1: " + str(graph_bp1.does_terminate()))
    print("terminaison de PC: " + str(graph_pc.does_terminate()))
    print("terminaison de bPC: " + str(graph_bpc.does_terminate()))
    cycles = loop_get_cycles(graph_pc.graph_dyna)
    for c in cycles:
        print(is_fair_cycle(graph_pc.graph_dyna, c))
    #print("présence d'une SDW: " + str(sdw_1TG(G, graph_pc)))
    #affichage_dyna(graph_pc.graph_dyna, "PC")"""

test2(lst)
"""a = Strategy({"s2"})
b = Strategy({"s3"})
G = nx.DiGraph()
G.add_edge(a,b)
"""

print()
#affichage_dyna(G)