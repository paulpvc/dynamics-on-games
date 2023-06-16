from util import *
from GraphDynamic import GraphDynamic
import networkx as nx


class GraphP1(GraphDynamic):
    def __init__(self, G: nx.DiGraph, strategies_profiles: tuple):
        super().__init__(G, strategies_profiles)
        self.graph_dyna = self.create_dyna()

    def create_dyna(self):
        dyna_P1 = nx.DiGraph()
        for id_strat_source in range(len(self.strategies_profiles[1])):
            strategy_source = self.strategies_profiles[2][id_strat_source]
            for id_strat_target in range(len(self.strategies_profiles[1])):
                strategy_target = self.strategies_profiles[2][id_strat_target]
                if self.is_edge(strategy_source, strategy_target, self):
                    #dyna_P1.add_edge(strategy_source, get_edge_name(strategy_target, self.G))
                    dyna_P1.add_edge(self.strategies_profiles[0][id_strat_source], self.strategies_profiles[0][id_strat_target])
        return dyna_P1

    @staticmethod
    def is_edge(strategy_source, strategy_target, self):
        difference = strategy_source.difference(strategy_target)
        if len(difference) == 1:
            player = difference.pop()[0]
            #print(player)
            if outcome(player, get_edge_name_set(strategy_source, self.G)) < outcome(player, get_edge_name_set(strategy_target, self.G)):
                return True
        return False



