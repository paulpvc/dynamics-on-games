from util import *
import my_networkx as nx


class Strategy:
    def __init__(self, strategy: set):
        self.strategy = strategy

    def __repr__(self):
        return "".join(self.strategy)