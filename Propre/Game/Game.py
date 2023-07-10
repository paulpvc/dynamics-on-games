from Propre.Utilities.util import *
from Propre.Game.Player import Player
from Propre.Game.Graph_P1 import GraphP1
from Propre.Game.Graph_PC import GraphPC
from Propre.Game.Graph_bP1 import GraphbP1
from Propre.Game.Graph_bPC import GraphbPC


class Game:
    def __init__(self,players:list[Player],edges:list,preferences: dict):
        self.game_graph = get_graph(players,edges)
        for player in players:
            if player in preferences.keys():
                player.set_preferences(preferences[player])
        nodes = get_nodes_of_dynamic_graph(self.game_graph)
        self.graph_of_dynamic_P1 = GraphP1(self.game_graph,nodes)
        self.graph_of_dynamic_bP1 = GraphbP1(self.game_graph, nodes)
        self.graph_of_dynamic_PC = GraphPC(self.game_graph, nodes)
        self.graph_of_dynamic_bPC = GraphbPC(self.game_graph, nodes)


    def display_game_graph(self):
        affichage(self.game_graph)

    def display_dynamic_graph_P1(self):
        affichage_dyna(self.graph_of_dynamic_P1.graph_dyna,"P1")
    def display_dynamic_graph_bP1(self):
        affichage_dyna(self.graph_of_dynamic_bP1.graph_dyna,"bP1")
    def display_dynamic_graph_PC(self):
        affichage_dyna(self.graph_of_dynamic_PC.graph_dyna,"PC")
    def display_dynamic_graph_bPC(self):
        affichage_dyna(self.graph_of_dynamic_bPC.graph_dyna,"bPC")

    def display_dynamics_terminations(self):
        """
        affiche dan sla console la terminaison des dynamiques
        :return: None
        """
        lst = [self.graph_of_dynamic_P1, self.graph_of_dynamic_bP1, self.graph_of_dynamic_PC, self.graph_of_dynamic_bPC]
        label = ["P1", "bP1", "PC", "bPC"]
        for i in range(len(lst)):
            print(f"terminaison de {label[i]}:", lst[i].does_terminate())

    def contain_dw_sdw(self):
        """
        heuristique pour déterminer la présence de dw et sdw dans un graphe
        (ne marche que dans certains cas particuliers)
        :return: bool
        """
        dw, sdw = find_dw_sdw(self.game_graph)
        print("présence d'une DW:", dw)
        print("présence d'une SDW:", sdw)
        return dw, sdw