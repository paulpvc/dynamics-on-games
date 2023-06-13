from util import *
import networkx as nx
from Graph_bP1 import GraphbP1

class GraphbPC:
    def __init__(self, G: nx.DiGraph, strategies_profiles: list[set]):
        self.G = G
        self.strategies_profiles = strategies_profiles
        self.graph_dyna = self.create_dyna()

    def create_dyna(self):
        dyna_bPC = nx.DiGraph()
        for strategy1 in self.strategies_profiles:
            for strategy2 in self.strategies_profiles:
                difference = strategy1.difference(strategy2)
                if len(difference) > 0:
                    if self.is_edge(strategy1, strategy2, difference):
                        dyna_bPC.add_edge(get_edge_name(strategy1, self.G), get_edge_name(strategy2, self.G))
        return dyna_bPC

    def is_edge(self, strategy1, strategy2, difference):
        difference2 = strategy2.difference(strategy1)
        best_bP1 = GraphbP1.get_best_strategy(self, strategy1)
        count = 0
        for edge1 in difference:
            for edge2 in difference2:
                if edge2[0] == edge1[0]:
                    temp = strategy1.copy()
                    temp.discard(edge1)
                    temp.add(edge2)
                    break
            if best_bP1[edge1[0]] == temp:
                count += 1
        if count == len(difference):
            return True
        return False

    def does_terminate(self):
        return not loop_cycle_detection(self.graph_dyna)

    def contain_fair_cycle(self):
        cycles = loop_get_cycles(self.graph_dyna)
        for cycle in cycles:
            if not is_fair_cycle(self.graph_dyna, cycle):
                return False
        return True
