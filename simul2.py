import networkx as nx
import my_networkx as my_nx
import matplotlib.pyplot as plt
from itertools import product

def affichage(G):
    pos = nx.spring_layout(G, seed=5)
    fig, ax = plt.subplots()
    nx.draw_networkx_nodes(G, pos, ax=ax)
    nx.draw_networkx_labels(G, pos, ax=ax)

    curved_edges = [edge for edge in G.edges()]
    nx.draw_networkx_edges(G, pos, edgelist=curved_edges, connectionstyle='arc3, rad=0.25')
    edge_weights = nx.get_edge_attributes(G, 'w')
    curved_edge_labels = {edge: edge_weights[edge] for edge in curved_edges}
    my_nx.my_draw_networkx_edge_labels(G, pos, ax=ax, edge_labels=curved_edge_labels, rotate=False, rad=0.25)
    plt.show()
def get_graph(nodes: list, edges: list[tuple]):
    graph = nx.DiGraph()
    graph.add_nodes_from(nodes)
    graph.add_edges_from(edges)
    return graph

def get_strategy_profiles(graph:nx.DiGraph):
     strategy_profiles = []
     players_actions = {}
     for node in list(graph.nodes):
         if graph.out_degree[node]>0:
            players_actions[node]= list(graph.edges([node]))
     strategy_profiles = [set(strategy) for strategy in (product(*players_actions.values()))]
     return strategy_profiles

def get_labelled_strategy_profiles(graph:nx.DiGraph):
    strategy_profiles =get_strategy_profiles(graph)
    labelled_strategy_profiles = []
    for strategy_profile in strategy_profiles:
        labels = set()
        for player_strategy in strategy_profile:
            labels.add(graph.get_edge_data(*(player_strategy))["w"])
        labelled_strategy_profiles.append(labels)
    return labelled_strategy_profiles

def is_edge(node1, node2,pref):
    if len(node1.intersection(node2)) == 1 and pref.index(node1) < pref.index(node2):
        return True
    return False

"""def get_dynamic_P1_graph(graph:nx.DiGraph):
    labelled_strategy_profiles = get_labelled_strategy_profiles(graph)
    dynamic_P1_graph = nx.DiGraph
    u = [''.join(list(e)) for e in labelled_strategy_profiles]
    dynamic_P1_graph.add_nodes_from(graph1,u)
    return dynamic_P1_graph """





preferences_1 = [{"c1","c2"},{"s1,s2"},{"c1","s2"}]
preferences_2 = [{"c2","c1"},{"s2,s1"},{"c2","s1"}]

graph1 = get_graph([1,2,3],[(1,2,{"w": "c1"}),(2,1,{"w": "c2"}),(1,3,{"w": "s1"}),(2,3,{"w": "s2"})])






