from util import *
import networkx as nx


class Player:
    def __init__(self, name: str, preference: list[set], actions: set):
        self.name = name
        self.preference = preference
        self.actions = actions