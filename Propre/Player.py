from util import *
import networkx as nx


class Player:
    def __init__(self, name):
        self.name = name
        self.preference = nx.DiGraph()
        self.pref_dict = dict()

    def set_preferences(self, preference):
        self.pref_dict = get_dict_preference(preference)
        matrix = get_preference_edges(preference, self.pref_dict)


        for i in range(len(matrix)):
            matrix[i][i] = 1

        matrix = get_final_matrix(matrix)

        lst = list(self.pref_dict.items())
        lst.sort(key=lambda x: x[1])
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if matrix[i][j]:
                    self.preference.add_edge(lst[i][0], lst[j][0])
        affichage_dyna(self.preference)

    def __repr__(self):
        return str(self.name)


