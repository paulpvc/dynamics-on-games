from util import *
import networkx as nx


class GraphP1:
    def __init__(self, G: nx.DiGraph, strategies_profiles: list[set]):
        self.G = G
        self.strategies_profiles = strategies_profiles
        self.graph_dyna = self.create_dyna()

    def create_dyna(self):
        dyna_P1 = nx.DiGraph()
        for strategy1 in self.strategies_profiles:
            for strategy2 in self.strategies_profiles:
                if self.is_edge(strategy1, strategy2):
                    dyna_P1.add_edge(get_edge_name(strategy1, self.G), get_edge_name(strategy2, self.G))
        return dyna_P1

    def is_edge(self, node1, node2):
        difference = node1.difference(node2)
        if len(difference) == 1:
            player = difference.pop()[0]
            if outcome(player.preference, node1) < outcome(player.preference, node2):
                return True
        return False

    def does_terminate(self):
        return not loop_cycle_detection(self.graph_dyna)

