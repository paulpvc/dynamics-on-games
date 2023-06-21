
from Player import Player
from Strategy import Strategy
from Game import Game
from util import is_n1tg

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
    print(game.graph_of_dynamic_PC.contains_fair_cycle())


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

    preferences = {player1: {strat3:1,strat2:1},
                   player2: {strat5:1,strat4:1}}

    game = Game(lst, edge_list, preferences)
    print(is_n1tg(game.game_graph))
test()