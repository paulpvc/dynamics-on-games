import networkx as nx
import my_networkx as my_nx
import matplotlib.pyplot as plt
from itertools import product
import numpy as np
from util import get_graph
from LinkedList import *


date = 0
color = {}


nodes = [1,2,3,4,5,6,7,]
edges = [(1,2),(2,3),(3,4),(4,1),(2,5),(5,6),(6,5),(5,7)]
G = get_graph(nodes,edges)

def visit_node_in_dfs(node, G:nx.DiGraph, color: dict,parents: dict, discovery_date:dict, treatment_end_date:dict,back_edges:set):
  color[node] = "g"
  global date
  date+=1
  discovery_date[node] = date
  for successor in list(G.successors(node)):
      if color[successor] == "w":
          parents[successor] = node
          visit_node_in_dfs(successor,G,color,parents,discovery_date,treatment_end_date,back_edges)
      elif color[successor] == "g":
          back_edges.add((node,successor))

  color[node] = "b"
  date+=1
  treatment_end_date[node] = date



def depth_first_search(G:nx.DiGraph):
    color = {node: "w" for node in list(G.nodes())}
    parents = {node: None for node in list(G.nodes)}
    discovery_date = {}
    treatment_end_date = {}
    back_edges = set()
    global date
    date = 0
    for node in list(G.nodes()):
        if color[node] == "w":
            visit_node_in_dfs(node,G,color,parents,discovery_date, treatment_end_date,back_edges)

    return {"parents":parents,
            "discovery_date":discovery_date,
            "treatment_end_date":treatment_end_date,
            "back_edges":back_edges
            }

def contains_cycle(G:nx.DiGraph):
    return len(depth_first_search(G)["back_edges"]) > 0


def topological_sorting (G:nx.DiGraph):
    treatment_end_date = depth_first_search(G)["treatment_end_date"]
    list_nodes = LinkedList()
    for node in treatment_end_date:
        list_nodes.prepend(node)
    return list_nodes


def visit_node_in_dfs_for_kosaraju(node,G: nx.DiGraph,parents:dict,color:dict,component):
    color[node] = "g"
    for successor in list(G.successors(node)):
        if color[successor] == "w":
            component.append(successor)
            parents[successor] = node
            visit_node_in_dfs_for_kosaraju(successor, G,parents,color,component)
    color[node] = "b"

def depth_first_search_for_kosaraju(G:nx.DiGraph,treatment_end_date:dict):
    color = {node: "w" for node in list(G.nodes())}
    parents = {node: None for node in list(G.nodes)}
    connected_components = []
    sorted_desc_treatment_end_date = dict(sorted(treatment_end_date.items(),key=lambda item: item[1],reverse=True))
    print(sorted_desc_treatment_end_date)
    for node in sorted_desc_treatment_end_date:
        if color[node] == "w":
            component = [node]
            visit_node_in_dfs_for_kosaraju(node,G,parents,color,component)
            connected_components.append(component)
    return connected_components


def kokosaraju(G:nx.DiGraph):
    treatment_end_date = depth_first_search(G)["treatment_end_date"]
    print(treatment_end_date)
    transpose = G.reverse()
    print(transpose)
    return depth_first_search_for_kosaraju(transpose,treatment_end_date)


print(kokosaraju(G))





