import networkx as nx
from util import *
from Player import Player
from Strategy import Strategy


class GraphDynamic:
    def __init__(self, G: nx.DiGraph, strategies_profiles):
        self.G = G
        self.strategies_profiles = strategies_profiles
        self.graph_dyna = None

    def does_terminate(self):
        """
            retourne un booléen déterminant si la dynamique se termine en cherchant la présence de cycle dans le
            graphe de dynamique
            :return: bool
        """
        return not loop_cycle_detection(self.graph_dyna)

    def contains_fair_cycle(self):
        """
        retourne un booléen déterminant si le graphe de dynamique contient un cycle équitable (vecteur pour savoir
        si la dynamique termine équitablement
        :return: bool
        """
        cycles = loop_get_cycles(self.graph_dyna)
        for cycle in cycles:
            if not is_fair_cycle(self.graph_dyna, cycle,list(self.G.nodes)):
                return False
        return True
