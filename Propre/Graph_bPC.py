from util import *
import networkx as nx
from Graph_bP1 import GraphbP1

class GraphbPC:
    def __init__(self, G: nx.DiGraph, strategies_profiles: tuple):
        self.G = G
        self.strategies_profiles = strategies_profiles
        self.graph_dyna = self.create_dyna()

    def create_dyna(self):
        dyna_bPC = nx.DiGraph()
        for id_strat_source in range(len(self.strategies_profiles[1])):
            strategy_source = self.strategies_profiles[2][id_strat_source]
            for id_strat_target in range(len(self.strategies_profiles[1])):
                strategy_target = self.strategies_profiles[2][id_strat_target]
                difference = strategy_source.difference(strategy_target)
                if len(difference) > 0:
                    if self.is_edge(strategy_source, strategy_target, difference):
                        dyna_bPC.add_edge(self.strategies_profiles[0][id_strat_source], self.strategies_profiles[0][id_strat_target])
        return dyna_bPC

    def is_edge(self, strategy_source, strategy_target, difference):
        difference2 = strategy_target.difference(strategy_source)
        best_bP1 = GraphbP1.get_best_strategy(self, strategy_source)
        count = 0
        #print(difference, difference2, best_bP1)
        for edge1 in difference:
            for edge2 in difference2:
                if edge2[0] == edge1[0]:
                    temp = strategy_source.copy()
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
