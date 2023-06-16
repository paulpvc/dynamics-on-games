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
        return not loop_cycle_detection(self.graph_dyna)

    def contain_fair_cycle(self):
        cycles = loop_get_cycles(self.graph_dyna)
        for cycle in cycles:
            if not is_fair_cycle(self.graph_dyna, cycle):
                return False
        return True
