from util import *
import networkx as nx
from algoGraphs import score

class Player:
    def __init__(self, name):
        self.name = name
        self.preference = nx.DiGraph()

    def set_preferences(self, preference):
        arcs = get_preference_edges(preference)

        self.preference.add_edges_from(arcs)
        affichage_dyna(self.preference, "rjdfodg")
        self.preference = score(self.preference)
        print("score: ",self.preference)

    def __repr__(self):
        return str(self.name)


