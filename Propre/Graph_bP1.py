from util import *
import networkx as nx
from Graph_P1 import GraphP1

class GraphbP1:
    def __init__(self, G: nx.DiGraph, strategies_profiles: tuple):
        self.G = G
        self.strategies_profiles = strategies_profiles
        self.graph_dyna = self.create_dyna()

    def create_dyna(self):
        dyna_bP1 = nx.DiGraph()
        for id_strat_source in range(len(self.strategies_profiles[1])):
            strategy_source = self.strategies_profiles[1][id_strat_source]
            best_reply = self.get_best_strategy(self, id_strat_source)
            for better_strategy in best_reply.values():
                if better_strategy is not None:
                    dyna_bP1.add_edge(self.strategies_profiles[0][id_strat_source], get_edge_name(better_strategy, self.G))
        return dyna_bP1

    @staticmethod
    def get_best_strategy(self, id_strat_source):
        strategy_source = self.strategies_profiles[2][id_strat_source]
        best_reply = {n: None for n in self.G.nodes()}
        for id_strat_target in range(len(self.strategies_profiles[1])):
            strategy_target = self.strategies_profiles[2][id_strat_target]
            if GraphP1.is_edge(id_strat_source, id_strat_target, self):
                player = strategy_source.difference(strategy_target).pop()[0]
                strategy_target_name = self.strategies_profiles[1][id_strat_target]
                if best_reply[player] is None or outcome(player, best_reply[player]) < outcome(player, strategy_target_name):
                    best_reply[player] = strategy_target
        return best_reply


    """@staticmethod
    def is_edge(node1, node2):
        difference = node1.difference(node2)
        if len(difference) == 1:
            player = difference.pop()[0]
            if outcome(player.preference, node1) < outcome(player.preference, node2):
                return True
        return False
    
    
    def is_egde_in_bp1(self,node1,node2,strategies):
        if GraphP1.is_edge(node1,node2):
            difference = node1.difference(node2)

            for strategy in strategies:
                if strategy != node2 and GraphP1.is_edge(node1, strategy):
                    pass"""
    def does_terminate(self):
        return not loop_cycle_detection(self.graph_dyna)

    def contain_fair_cycle(self):
        cycles = loop_get_cycles(self.graph_dyna)
        for cycle in cycles:
            if not is_fair_cycle(self.graph_dyna, cycle):
                return False
        return True
