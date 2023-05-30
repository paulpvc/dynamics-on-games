import networkx as nx
import my_networkx as my_nx
import matplotlib.pyplot as plt
from itertools import product
from util import *





def get_graph(nodes: list, edges: list[tuple]):
    graph = nx.DiGraph()
    graph.add_nodes_from(nodes)
    graph.add_edges_from(edges)
    return graph

def get_strategy_profiles(graph:nx.DiGraph):
     strategy_profiles = []
     players_actions = {}
     for node in list(graph.nodes):
         if graph.out_degree[node] > 0:
            players_actions[node] = list(graph.edges([node]))
     strategy_profiles =  [strategy_profile for strategy_profile in (product(*players_actions.values()))]
     return strategy_profiles


def get_nodes_of_dynamic_graph(graph:nx.DiGraph):
    nodes = []
    set_of_edges_label = set()
    my_list = []
    node_label_content = []
    strategy_profiles = get_strategy_profiles(graph)
    for strategy_profile in strategy_profiles:
        for player_strategy in strategy_profile:
            temp = graph.get_edge_data(*player_strategy)["w"]
            node_label_content.append(temp)
            set_of_edges_label.add(temp)
        nodes.append(''.join(node_label_content))
        my_list.append(set_of_edges_label)
        node_label_content = []
        set_of_edges_label = set()
    return nodes,my_list


def get_edges_of_dynamic_P1_graph(graph:nx.DiGraph, preferences):
     edges = []
     nodes, my_list = get_nodes_of_dynamic_graph(graph)
     for p in range(len(preferences)):
         for i in range(len(my_list)):
             for j in range(len(my_list)):
                 if is_edge_in_P1(my_list[i],my_list[j],p+1,preferences[p]):
                     edges.append((nodes[i],nodes[j]))
     return edges

def get_payoff(strategy:set, preference:list[set]):
    payoff = -1
    for i in range(len(preference)):
        if preference[i].issubset(strategy):
            payoff = i
    return payoff

def is_edge_in_P1(node1, node2,player,pref):
    my_set = node1.intersection(node2)
    if  len(my_set) == 1 and not list(my_set)[0].endswith(str(player))  and get_payoff(node1,pref) < get_payoff(node2,pref):
        return True
    return False







preferences_1 = [{"c1","c2"},{"s1"},{"c1","s2"}]
preferences_2 = [{"c2","c1"},{"s2"},{"c2","s1"}]
preferences = [preferences_1,preferences_2]

graph1 = get_graph([1,2,3],[(1,2,{"w": "c1"}),(2,1,{"w": "c2"}),(1,3,{"w": "s1"}),(2,3,{"w": "s2"})])

print(get_edges_of_dynamic_P1_graph(graph1,preferences))

graph2 = get_graph(get_nodes_of_dynamic_graph(graph1)[0],get_edges_of_dynamic_P1_graph(graph1,preferences))

print(graph2)
affichage_dyna(graph2)






