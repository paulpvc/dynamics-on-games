from util import *
import networkx as nx


class Player:
    def __init__(self, name, actions: set):
        self.name = name
        self.preference = []
        self.actions = actions

    def set_preferences(self, preference: list[set]):
        self.preference = preference

    def __repr__(self):
        return str(self.name)