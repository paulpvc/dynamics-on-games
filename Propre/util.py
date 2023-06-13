import networkx as nx
import my_networkx as my_nx
import matplotlib.pyplot as plt
from itertools import product
import numpy as np
from Pile import Pile



def get_graph(nodes: list, edges: list[tuple]):
    graph = nx.DiGraph()
    graph.add_nodes_from(nodes)
    graph.add_edges_from(edges)
    return graph


def outcome(G: nx.DiGraph, preference: nx.DiGraph, strategy: set, strategy2: set):
    strategy = get_edge_name_set(strategy, G)
    strategy2 = get_edge_name_set(strategy2, G)
    ids = [None, None]
    strats = [strategy,strategy2]
    for pref_strat in preference.nodes():
        for strat_i in range(len(strats)):
            if pref_strat.strategy.issubset(strats[strat_i]):
                ids[strat_i] = pref_strat
                break
        if len(strats) == 0:
            break
    if ids[0] is None and ids[1] is not None:
        return True
    elif ids[1] is None and ids[0] is not None:
        return False

    return preference.has_edge(ids[0], ids[1])

def get_edge_name_set(edges: set, G: nx.DiGraph):
    res = set()
    for edge in edges:
        res.add(G.get_edge_data(*edge)["w"])
    return res

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

    for node in list(graph.nodes):
        if graph.out_degree[node] > 0:
            players_actions[node] = list(graph.edges([node]))
    strategy_profiles = [set(strategy_profile) for strategy_profile in (product(*players_actions.values()))]
    return strategy_profiles

def get_dict_index(strat: set, pref_dict: dict):
    for id, strat_temp in pref_dict.items():
        if strat == strat_temp:
            return id
    return -1

def get_preference_edges(preference, pref_dict: dict):
    arcs = [[0]*len(pref_dict) for _ in range(len(pref_dict))]
    for pref_tuple in preference:
        for i in range(len(pref_tuple)-1):
            id_x = pref_dict[pref_tuple[i]]
            id_y = pref_dict[pref_tuple[i+1]]
            arcs[id_x][id_y] = 1
            """arc = (get_dict_index(pref_tuple[i], pref_dict), get_dict_index(pref_tuple[i+1], pref_dict))
            arcs.append(arc)"""
    return arcs


def get_dict_preference(preferences: list):
    resultat = dict()
    count = 0
    for tpl in preferences:

        for strat in tpl:
            if strat not in resultat:
                resultat[strat] = count
                count +=1
    return resultat


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


def get_product_matrix(mat1,mat2):
    mat1_row = len(mat1)
    mat1_columm = len(mat1[0])
    mat2_row = len(mat2)
    mat2_column = len(mat2[0])
    if mat1_columm != mat2_row:
        return -1
    result = np.zeros((mat1_row,mat2_column))
    for i in range(mat1_row):
        for j in range(mat2_column):
            for k in range(mat1_columm):
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

def pull_max_pref(player, label):
    max_pref = None
    for strategy in player.preference:
        if label in strategy.strategy:
            if max_pref is None or player.preference[max_pref] < player.preference[strategy]:
                max_pref = strategy
    return max_pref


def stuck_in_cycle(G: nx.DiGraph, cycle: list, player):
    d = {p[2]: p[:2] for p in G.edges.data(nbunch=player, data="w", default="")}
    max_out, max_in = 0, 0
    for label in d:
        temp = pull_max_pref(player, label)
        if d[label][1] in cycle:
            if player.preference[temp] > max_in:
                max_in = player.preference[temp]
        else:
            if player.preference[temp] > max_out:
                max_out = player.preference[temp]
    return max_in > max_out #ambiguité si équivalence entre les chemins, on suppose que il va sortir si possible


def find_dw(G: nx.DiGraph):
    cycles = loop_get_cycles(G)

    for cycle in cycles:
        dw = True
        for player in cycle:
            if not stuck_in_cycle(G, cycle, player):
                dw = False
                break
        if dw:
            return True
    return False




def dfs_kosaraju_stack(G, node, seen:dict, stack):
    seen[node] = True
    for n in G.neighbors(node):
        if not seen[n]:
            dfs_kosaraju_stack(G, n, seen, stack)
    stack.push(node)


def dfs_kosaraju_list(G, node, seen, scc):
    seen[node] = True
    for n in G.neighbors(node):
        if not seen[n]:
            dfs_kosaraju_list(G, node, seen, scc)
    scc.append(node)


def kosaraju(G: nx.DiGraph):
    stack = Pile()
    seen = {n: False for n in G.nodes()}
    for node in G.nodes():
        if not seen[node]:
            dfs_kosaraju_stack(G, node, seen, stack)

    transpose = G.reverse()
    seen = {n: False for n in G.nodes()}
    scc_list = []
    while not stack.is_empty():
        node = stack.pull()
        scc = []
        if not seen[node]:
            dfs_kosaraju_list(transpose, node, seen, scc)
            scc_list.append(scc)
    return scc_list