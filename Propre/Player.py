from util import *
import networkx as nx


class Player:
    def __init__(self, name):
        self.name = name
        self.preference = [] #a refaire
        self.preference_graph = nx.DiGraph()

    def set_preferences(self, preference: list[set[str]], G: nx.DiGraph):
        self.preference = preference
        arcs = get_edge_by_name(G, preference)
        self.preference = arcs

    def __repr__(self):
        return str(self.name)


