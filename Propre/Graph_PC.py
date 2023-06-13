from util import *
import networkx as nx
from Graph_P1 import GraphP1


class GraphPC:
    def __init__(self, G: nx.DiGraph, strategies_profiles: list[set]):
        self.G = G
        self.strategies_profiles = strategies_profiles
        self.graph_dyna = self.create_dyna()

    def create_dyna(self):
        dyna_PC = nx.DiGraph()
        for strategy1 in self.strategies_profiles:
            for strategy2 in self.strategies_profiles:
                if self.is_edge(self.G, strategy1, strategy2):
                    dyna_PC.add_edge(get_edge_name(strategy1, self.G), get_edge_name(strategy2, self.G))
        return dyna_PC

    @staticmethod
    def is_edge(G, node1, node2):
        if node1 == node2:
            return False
        players = list(filter(lambda x: (G.out_degree[x] > 0), G.nodes))
        player_updating_their_strategy_actions = node2.difference(node1)
        nb_player_updating_their_strategy = len(player_updating_their_strategy_actions)
        counter = 0
        for player in players:
            player_edges = set(G.edges([player]))
            player_update = player_edges.intersection(player_updating_their_strategy_actions)
            other_players_actions = node1.difference(player_edges)
            if len(player_update) == 1:
                other_players_actions.add(*player_update)
                if GraphP1.is_edge(node1, other_players_actions, G):
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



