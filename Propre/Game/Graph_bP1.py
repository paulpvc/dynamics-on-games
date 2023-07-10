from Propre.Utilities.util import *
import networkx as nx
from Propre.Game.Graph_P1 import GraphP1
from Propre.Game.GraphDynamic import GraphDynamic


class GraphbP1(GraphDynamic):
    def __init__(self, G: nx.DiGraph, strategies_profiles: tuple):
        super().__init__(G, strategies_profiles)
        self.graph_dyna = self.create_dyna()

    def create_dyna(self):
        dyna_bP1 = nx.DiGraph()
        for id_strat_source in range(len(self.strategies_profiles[1])):
            strategy_source = self.strategies_profiles[2][id_strat_source]
            best_reply = self.get_best_strategy(self, strategy_source)
            #print(best_reply)
            for better_strategy in best_reply.values():
                if better_strategy is not None:
                    dyna_bP1.add_edge(self.strategies_profiles[0][id_strat_source], get_edge_name(better_strategy, self.G))
        return dyna_bP1

    @staticmethod
    def get_best_strategy(self, strategy_source):
        best_reply = {n: None for n in self.G.nodes()}
        for id_strat_target in range(len(self.strategies_profiles[1])):
            strategy_target = self.strategies_profiles[2][id_strat_target]
            #print(GraphP1.is_edge(strategy_source, strategy_target, self))
            if GraphP1.is_edge(strategy_source, strategy_target, self):
                player = strategy_source.difference(strategy_target).pop()[0]
                strategy_target_name = get_edge_name_set(strategy_target, self.G)
                #print(player, best_reply[player], strategy_target_name)
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
