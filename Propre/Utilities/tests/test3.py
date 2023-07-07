from Propre.Game.Player import Player
from Propre.Game.Strategy import Strategy
from Propre.Game.Game import Game
from util import *

def test():
    player1 = Player("v1")
    player2 = Player("v2")
    player3 = Player("v3")
    playerB = Player("vb")
    lst = [player1, player2,player3, playerB]



    edge_list = [(player1,player2,{"w": "c1"}),(player2,player3,{"w": "c2"}),(player3,player1, {"w":"c3"}),(player1,playerB,{"w": "s1"}),(player2,playerB,{"w": "s2"}),(player3,playerB,{"w": "s3"})]

    strat3 = Strategy({"c1", "s2"})
    strat4 = Strategy({"s1", "c2", "c3"})
    strat5 = Strategy({"s2"})
    strat2 = Strategy({"s1"})
    strat6 = Strategy({"s3"})
    strat7 = Strategy({"c3", "s1"})

    preferences = {player1: [(strat2, strat3)],
                   player2: [(strat5, strat4)],
                   player3: [(strat6,)]}

    game = Game(lst,edge_list,preferences)

    #game.display_game_graph()
    #game.display_dynamic_graph_PC()
    #game.contain_dw_sdw()
    #print(game.graph_of_dynamic_PC.contains_fair_cycle())
    print(game.graph_of_dynamic_PC.does_fairly_terminate())


def test2():
    player1 = Player("v1")
    player2 = Player("v2")
    playerB = Player("vb")
    lst = [player1, player2, playerB]

    edge_list = [(player1, player2, {"w": "c1"}), (player2, player1, {"w": "c2"}), (player1, playerB, {"w": "s1"}),
                 (player2, playerB, {"w": "s2"})]

    strat3 = Strategy({"c1", "s2"})
    strat4 = Strategy({"s1", "c2"})
    strat5 = Strategy({"s2"})
    strat2 = Strategy({"s1"})


    preferences = {player1: {strat3:1,strat2:2}, #marche pas si strat2:2 alors que ça devrait marcher car c'est pas le même arc sortant
                   player2: {strat5:1,strat4:1}}

    game = Game(lst, edge_list, preferences)
    print(is_n1tg(game.game_graph))


def affichage_temp(G):
    pos = nx.planar_layout(G)
    pos["p7"][0] -= 1
    pos["p6"][0] -= 0.3
    pos["p1"][0] += 1
    fig, ax = plt.subplots()
    nx.draw_networkx_nodes(G, pos, ax=ax)
    nx.draw_networkx_labels(G, pos, ax=ax)
    curved_edges = [edge for edge in G.edges()]
    nx.draw_networkx_edges(G, pos, edgelist=curved_edges, connectionstyle='arc3, rad=0.25')
    plt.show()

def test4():
    pref_g = nx.DiGraph()
    for i in range(1, 8):
        pref_g.add_node(f"p{i}")
    edges = [("p1","p2"), ("p1", "p3"), ("p2", "p3"),("p3","p2"), ("p3", "p4"), ("p4", "p5"), ("p5", "p4"), ("p4", "p6"),
             ("p6", "p4"), ("p5", "p6"),("p6","p5"), ("p7", "p5")]
    pref_g.add_edges_from(edges)
    affichage_temp(pref_g)

test4()