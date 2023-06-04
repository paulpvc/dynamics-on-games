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
                 if i !=j and is_edge_in_P1(my_list[i],my_list[j],p+1,preferences[p]):
                     edges.append((nodes[i],nodes[j]))
     return edges

def get_payoff(strategy:set, preference:list[set]):
    payoff = -1
    for i in range(len(preference)):
        if preference[i].issubset(strategy):
            payoff = i
    return payoff

def is_edge_in_P1(node1, node2,player,pref):
    my_set = node2.difference(node1)
    print("gain du premier noeud:", get_payoff(node1,pref))
    print("gain du 2ème noeud:", get_payoff(node2, pref))
    if  len(my_set) == 1 and  list(my_set)[0].endswith(str(player))  and get_payoff(node1,pref) < get_payoff(node2,pref):
        return True
    return False


def get_edges_of_dynamic_PC_graph(graph: nx.DiGraph, preferences,players):
    edges = []
    nodes, my_list = get_nodes_of_dynamic_graph(graph)
    for i in range(len(my_list)):
            for j in range(len(my_list)):
                if is_edge_in_pc(my_list[i], my_list[j],players, preferences):
                        edges.append((nodes[i], nodes[j]))
    return edges


def is_edge_in_pc(node1,node2,players:dict,pref):
    if node1 ==node2:
        return False
    player_updating_their_strategy_actions = node2.difference(node1)
    print("Joueurs changeant de stratégies(actions)",player_updating_their_strategy_actions)
    player_updating_their_strategy = len(player_updating_their_strategy_actions)
    print("Nombre",player_updating_their_strategy)
    counter = 0
    for player in players:
        player_update = players[player].intersection(player_updating_their_strategy_actions)
        other_players_actions = node1.difference(players[player])
        print("autres actions",other_players_actions)
        if len(player_update)== 1:
                other_players_actions.add(*player_update)
                print(other_players_actions)
                if  is_edge_in_P1(node1,other_players_actions ,player,pref[player-1]):
                    counter+=1
                other_players_actions.discard(*player_update)
    if counter == player_updating_their_strategy:
        return True
    return False








players = {1:{"c1","s1"},2:{"c2","s2"},3:{"c3","s3"}}

preferences_1 = [{"c1","c2","c3"},{"s1"},{"c1","s2"}]
preferences_2 = [{"c2","c1","c3"},{"s2"},{"c2","s1","c3"}]
preferences_3 = [{"c1","c2","c3"},{"s3"}]
preferences = [preferences_1,preferences_2,preferences_3]



arcs = [(1,2,{"w": "c1"}),(2,3,{"w":"c2"}),(3,1,{"w": "c3"}),(1,4,{"w": "s1"}),(2,4,{"w": "s2"}),(3,4,{"w":"s3"})]
graph1 = get_graph([1,2,3,4],arcs)

"""
print(get_edges_of_dynamic_P1_graph(graph1,preferences))
print()

graph2 = get_graph(get_nodes_of_dynamic_graph(graph1)[0],get_edges_of_dynamic_P1_graph(graph1,preferences)) 

graph3 = get_graph(get_nodes_of_dynamic_graph(graph1)[0],get_edges_of_dynamic_PC_graph(graph1,preferences))

print(graph2)
print(get_nodes_of_dynamic_graph(graph1)[1]," ",get_nodes_of_dynamic_graph(graph1)[0])
affichage_dyna(graph3)

print(get_strategy_profiles(graph1))"""


graph4 = get_graph(get_nodes_of_dynamic_graph(graph1)[0],get_edges_of_dynamic_PC_graph(graph1,preferences,players))
graph5 = get_graph(get_nodes_of_dynamic_graph(graph1)[0],get_edges_of_dynamic_P1_graph(graph1,preferences))
affichage_dyna(graph5,"p1")
#print(get_strategy_profiles(graph1))
"""print(is_edge_in_pc({"c1","c2","c3"},{"s1","s2","s3"},players,preferences))
print(is_edge_in_P1({"c1","c2","c3"},{"s1","c2","c3"},1,preferences[0]))"""








