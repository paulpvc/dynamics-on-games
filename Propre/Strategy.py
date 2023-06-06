from util import *
import networkx as nx

class Strategy:

    def __init__(self, strategy: set, id: int):
        self.id = id
        self.value = strategy
