from util import *
import networkx as nx


class Player:
    def __init__(self, name):
        self.name = name
        self.preference = nx.DiGraph()
        self.pref_dict = dict()

    def set_preferences(self, preference):
        self.pref_dict = get_dict_preference(preference)
        arcs = get_preference_edges(preference, self.pref_dict)
        self.preference.add_edges_from(arcs)

        matrix = nx.to_numpy_array(self.preference)
        for i in range(len(matrix)):
            matrix[i][i] = 1

        matrix = get_final_matrix(matrix)

        self.preference = nx.from_numpy_array(matrix, create_using=nx.DiGraph)
        affichage_dyna(self.preference)

    def __repr__(self):
        return str(self.name)


