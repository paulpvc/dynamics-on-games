import networkx as nx
import my_networkx as my_nx
import matplotlib.pyplot as plt
from itertools import product
import numpy as np



def get_graph(nodes: list, edges: list[tuple]):
    graph = nx.DiGraph()
    graph.add_nodes_from(nodes)
    graph.add_edges_from(edges)
    return graph

def outcome(preference: list, strategy: set):
    """
    calcul du gain pour la stratégie donnée en fonction de la préférence du joueur donnée (key)
    :param preferences: préférences de tous les joueurs
    :param strategy: la strategy dont on veut savoir l'outcome
    :return: int: outcome de la stratégie
    """
    for j in range(len(preference)):
        pref = preference[j]
        if pref.issubset(strategy):
            return j
    return -1


def get_edge_name(edges: set, G: nx.DiGraph):
    res = ""
    for edge in edges:
        res += G.get_edge_data(*edge)["w"]
    return res


def loop_cycle_detection(G: nx.DiGraph):
    """
    fonction déterminant la présence de cycle dans un graphe orienté, piur ça on exécute un parcours en profondeur
    sur le graphe depuis chaques noeuds (loop dans le nom)
    :param G: le graphe à analyser
    :return: booléen pour savoir si il y a un cycle
    """
    seen = {node: False for node in list(G.nodes())}
    current_path = {node: False for node in list(G.nodes())}
    for node in G.nodes():
        if not seen[node]:
            if cycle_detection(G, node, seen, current_path):
                return True
    return False


def cycle_detection(G, source, seen: dict, current_path: dict):
    """
    fonction récursive éffectuant le DFS en retenant les noeuds déjà parcouru et le chemin actuel
    :param G: le graphe à parcourir
    :param source: le noeud actuel (de départ)
    :param seen: le dict des noeuds déjà parcouru
    :param current_path: dict indiquant quels noeuds font partie du chemin actuel
    :return: booléan attestant si il y a un cycle dans le graphe
    """
    seen[source] = True
    current_path[source] = True

    for node in G.neighbors(source):
        if not seen[node]:
            if cycle_detection(G, node, seen, current_path):
                return True
        elif current_path[node]:
            return True
    current_path[source] = False
    return False


def get_strategy_profiles(graph: nx.DiGraph):
    players_actions = {}
    print(list(graph.nodes))
    for node in list(graph.nodes):
        if graph.out_degree[node] > 0:
            players_actions[node] = list(graph.edges([node]))
    strategy_profiles = [set(strategy_profile) for strategy_profile in (product(*players_actions.values()))]
    return strategy_profiles

def get_preferencce_edges(preference):
    arcs = []
    for pref_tuple in preference:
        for i in range(len(pref_tuple)-1):
            arc = (pref_tuple[i].id, pref_tuple[i+1].id)
            arcs.append(arc)
    return arcs


"""def get_nodes_of_dynamic_graph(graph: nx.DiGraph):
    nodes = []
    my_list = []
    strategy_profiles = get_strategy_profiles(graph)
    for strategy_profile in strategy_profiles:
        node_label_content = []
        set_of_edges_label = set()
        for player_strategy in strategy_profile:
            temp = graph.get_edge_data(*player_strategy)["w"]
            node_label_content.append(temp)
            set_of_edges_label.add(temp)
        nodes.append(''.join(node_label_content))
        my_list.append(set_of_edges_label)

    return nodes, my_list
"""

def affichage(G, title=""):
    """
    affichage d'un graphe orienté avec des noms pour les arcs
    :param G: graphe à afficher (arcs possédant tous des noms)
    :return: None
    """
    pos = nx.spring_layout(G, seed=5)
    fig, ax = plt.subplots()
    nx.draw_networkx_nodes(G, pos, ax=ax)
    nx.draw_networkx_labels(G, pos, ax=ax)

    curved_edges = [edge for edge in G.edges()]
    nx.draw_networkx_edges(G, pos, edgelist=curved_edges, connectionstyle='arc3, rad=0.25')
    edge_weights = nx.get_edge_attributes(G, 'w')
    curved_edge_labels = {edge: edge_weights[edge] for edge in curved_edges}
    my_nx.my_draw_networkx_edge_labels(G, pos, ax=ax, edge_labels=curved_edge_labels, rotate=False, rad=0.25)
    plt.title(title)
    plt.show()

def affichage_dyna(G, title=""):
    """
    affichage d'un graphe orienté pour les dynamiques (arcs sans nom)
    :param G: graphe d'une dynamique à afficher
    :return: None
    """
    pos = nx.spring_layout(G, seed=5, k=5)
    fig, ax = plt.subplots()
    nx.draw_networkx_nodes(G, pos, ax=ax)
    nx.draw_networkx_labels(G, pos, ax=ax)

    curved_edges = [edge for edge in G.edges()]
    nx.draw_networkx_edges(G, pos, edgelist=curved_edges, connectionstyle='arc3, rad=0.25', arrows=True)
    plt.title(title)
    plt.show()


def dfs(G: nx.DiGraph, source, seen: dict, cycle: list):
    seen[source] = True
    if G.out_degree(source) == 0 and G.in_degree(source) > 0:
        return True
    for node in G.neighbors(source):

        if node in cycle:
            #TODO Verifier que c'est une condition nécéssaire car il existe des graphes pour lesquels Gdis est mineur
            #Il faut surement rajouter la notion de préférence parce que c'est trop général?
            return False
        elif not seen[node]:
            if dfs(G, node, seen, cycle):
                return True
    return False

def loop_get_cycles(G: nx.DiGraph):
    seen = {node: False for node in list(G.nodes())}
    current_path = []
    path_id = {n: -1 for n in G.nodes()}
    cycles = []
    for node in G.nodes():
        if not seen[node]:
            cycle = get_cycles(G, node, seen, current_path, path_id)
            if len(cycle) > 0:
                cycles.append(cycle)
    return cycles


def get_cycles(G: nx.DiGraph, source, seen: dict, current_path: list, id_dict: dict):
    seen[source] = True
    current_path.append(source)
    id_dict[source] = len(current_path)-1
    for node in G.neighbors(source):
        if not seen[node]:
            temp = get_cycles(G, node, seen, current_path, id_dict)
            if len(temp) > 0:
                return temp
        elif id_dict[node] > -1:
            return current_path[id_dict[node]:]
    current_path.pop(-1)
    id_dict[source] = -1
    return []
# pour de l affichage il suffit de récupérer les edge_data pour obtenir les noms des arcs et pouvoir les plots comme il faut

def get_product_matrix(mat1,mat2):
    if len(mat1[0]) == len(mat2):
        return -1
    result = []
    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            for k in range(len(mat2)):
                result[i][j]+=mat1[i][k]*mat2[k][j]
            if result[i][j]>0:
                result[i][j]=1
    return result




def get_final_matrix(m: np.ndarray):
    square_of_m = get_product_matrix(m,m)
    while(not np.array_equal(m,square_of_m)):
        m = square_of_m
        square_of_m = get_product_matrix(square_of_m,square_of_m)
    return m




def find_dw(G: nx.DiGraph):
    cycles = loop_get_cycles(G)
    for cycle in cycles:
        count = 0
        for source in cycle:
            for node in G.neighbors(source):
                seen = {n: False for n in G.nodes()}

                if dfs(G, node, seen, cycle):
                    count += 1
                    if count == 2:
                        return True
    return False