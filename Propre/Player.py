from util import *
import networkx as nx
from algoGraphs import get_connected_components_graph, topological_sorting

class Player:
    def __init__(self, name):
        self.name = name
        self.preference = nx.DiGraph()
        self.pref_dict = dict()

    def set_preferences(self, preference):
        arcs = get_preference_edges(preference)

        self.preference.add_edges_from(arcs)
        self.preference = topological_sorting(get_connected_components_graph(self.preference)[0])

    def __repr__(self):
        return str(self.name)


