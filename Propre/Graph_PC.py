from util import *
import networkx as nx
from Graph_P1 import GraphP1


class GraphPC:
    def __init__(self, G: nx.DiGraph, strategies_profiles: tuple):
        self.G = G
        self.strategies_profiles = strategies_profiles
        self.graph_dyna = self.create_dyna()

    def create_dyna(self):
        dyna_PC = nx.DiGraph()
        for id_strat_source in range(len(self.strategies_profiles[1])):
            for id_strat_target in range(len(self.strategies_profiles[1])):
                if self.is_edge(self, id_strat_source, id_strat_target):
                    dyna_PC.add_edge(self.strategies_profiles[0][id_strat_source], self.strategies_profiles[0][id_strat_target])
        return dyna_PC

    @staticmethod
    def is_edge(self, id_strat_source, id_strat_target):
        strategy_source = self.strategies_profiles[2][id_strat_source]
        strategy_target = self.strategies_profiles[2][id_strat_target]
        if strategy_source == strategy_target:
            return False
        players = list(filter(lambda x: (self.G.out_degree[x] > 0), self.G.nodes))
        player_updating_their_strategy_actions = strategy_target.difference(strategy_source)
        nb_player_updating_their_strategy = len(player_updating_their_strategy_actions)
        counter = 0
        for player in players:
            player_edges = set(self.G.edges([player]))
            #print(player_edges)
            player_update = player_edges.intersection(player_updating_their_strategy_actions)
            other_players_actions = strategy_source.difference(player_edges)
            if len(player_update) == 1:
                other_players_actions.add(*player_update)
                if GraphP1.is_edge(strategy_source, other_players_actions, self):
                    counter += 1
                other_players_actions.discard(*player_update)
        if counter == nb_player_updating_their_strategy:
            return True
        return False

    def does_terminate(self):
        return not loop_cycle_detection(self.graph_dyna)

    def sdw_1TG(self):
        return not self.does_terminate()

    def contain_fair_cycle(self):
        cycles = loop_get_cycles(self.graph_dyna)
        for cycle in cycles:
            if not is_fair_cycle(self.graph_dyna, cycle):
                return False
        return True



