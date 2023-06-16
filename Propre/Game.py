from util import *
from Player import Player
from Strategy import Strategy
from Graph_P1 import GraphP1
from Graph_PC import GraphPC
from Graph_bP1 import GraphbP1
from Graph_bPC import GraphbPC


class Game:
    def __init__(self,players:list[Player],edges:list,preferences:dict):
        self.game_graph = get_graph(players,edges)
        for player in players:
            if player in preferences.keys():
                player.set_preferences(preferences[player])
        self.graph_of_dynamic_P1 = GraphP1(self.game_graph,get_nodes_of_dynamic_graph(self.game_graph)).graph_dyna
        self.graph_of_dynamic_bP1 = GraphbP1(self.game_graph, get_nodes_of_dynamic_graph(self.game_graph)).graph_dyna
        self.graph_of_dynamic_PC = GraphPC(self.game_graph, get_nodes_of_dynamic_graph(self.game_graph)).graph_dyna
        self.graph_of_dynamic_bPC = GraphPC(self.game_graph, get_nodes_of_dynamic_graph(self.game_graph)).graph_dyna

    def display_game_graph(self):
        affichage(self.game_graph)

    def display_dynamic_graph(self,dynamic_graph):
        affichage_dyna(dynamic_graph,"")