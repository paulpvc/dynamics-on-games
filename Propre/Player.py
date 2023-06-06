from util import *
import networkx as nx


class Player:
    def __init__(self, name):
        self.name = name
        self.preference = nx.DiGraph()

    def set_preferences(self, preference):
        arcs = get_preferencce_edges(preference)
        self.preference.add_edges_from(arcs)
        matrix = nx.to_numpy_array(self.preference)
        for i in range(len(matrix)):
            matrix[i][i] = 1
        #matrix = nx.from_numpy_array(matrix, create_using=nx.DiGraph)
        print(matrix)
        print("-----------------")
        matrix = get_final_matrix(matrix)
        print(matrix)
        self.preference = nx.from_numpy_array(matrix, create_using=nx.DiGraph)
        affichage_dyna(self.preference)

    def __repr__(self):
        return str(self.name)


