import networkx as nx
import my_networkx as my_nx
import matplotlib.pyplot as plt
from itertools import product
import numpy as np
from Pile import Pile


def get_graph(nodes: list, edges: list[tuple]):
    """
    fonction de construction d'un graphe avec des noeuds donnés et des arcs donnés
    :param nodes: liste des noeuds du graphe
    :param edges: liste des arcs entre les noeuds du graphe
    :return: un graphe de type networkx.DiGraph
    """
    graph = nx.DiGraph()
    graph.add_nodes_from(nodes)
    graph.add_edges_from(edges)
    return graph


def outcome(player, strategy: set):
    """
    fonction renvoyant le score de la strategy par rapport aux préférence du player passé en paramètre, en cherchant
    la strategie dans les préférences du joueur correspondant à la strategy passé en paramètre
    :param player: objet Player dont on utilise les préférences
    :param strategy: objet Strategy a déterminer le scoe
    :return: int : score correspondant à la strategy
    """

    #temp_strat = get_edge_name_set(strategy, G)
    for preference in player.preference:

        if preference.strategy.issubset(strategy):
            #rint(preference.strategy, strategy, player.preference[preference])
            return player.preference[preference]

    return -1


def get_edge_name_set(edges: set, G: nx.DiGraph):
    """
    fonction renvoyant le set des noms des arcs du set d'arcs passé en paramètre
    :param edges: set des arcs dont on cherche les noms
    :param G: Graphe de jeu de type networkx.DiGraph
    :return: set[string]: contenant les noms des arcs du set edges
    """
    res = set()
    for edge in edges:
        res.add(G.get_edge_data(*edge)["w"])
    return res


def get_edge_name(edges: set, G: nx.DiGraph):
    """
    foniton renvoyant le nom du chemin edges passé en paramètre, ce nom correspond a la concaténation des noms des arcs
    constituant le chemin edges
    :param edges: set d'arcs dont on cherche le nom du chemin
    :param G: Graphe de jeu de type networkx.DiGraph
    :return: str: nom du chemin en string
    """
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
    """
    fonction permettant de calculer et renvoyer une liste de tous les profils de stratégies en fonctions des chemins
    possibles
    :param graph: graphe de Jeu
    :return: liste des profils de stratégies
    """
    players_actions = {}

    for node in list(graph.nodes):
        if graph.out_degree[node] > 0:
            players_actions[node] = list(graph.edges([node]))
    strategy_profiles = [strategy_profile for strategy_profile in (product(*players_actions.values()))]
    return strategy_profiles


def get_dict_index(strat: set, pref_dict: dict):
    """
    fonction permettant de récupérer l'index d'une stratégie dans un dictionnaire de préférence(-1 si pas présent)
    :param strat: la stratégie à trouver
    :param pref_dict: dictionnaire de préférence
    :return: indice de la stratégie: int
    """
    for id, strat_temp in pref_dict.items():
        if strat == strat_temp:
            return id
    return -1


def get_preference_edges(preference):
    """
    fonction renvoyant une liste d'arcs depusi une liste de tuple où les tuples sont de taille n, et représentent
    les relations de préférences directe entre les chemins possibles d'un joueur
    :param preference: liste de tuples des préférences d'un chemins par rapport à d'autres
    :return: liste de tuple de taille 2 étant des arcs d'un graphe de préférence
    """
    arcs = []
    for pref_tuple in preference:
        if len(pref_tuple) == 1:
            arcs.append((pref_tuple[0], pref_tuple[0]))
        else:
            for i in range(len(pref_tuple)-1):
                arc = (pref_tuple[i], pref_tuple[i+1])
                arcs.append(arc)
    return arcs


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
    nx.draw_networkx_nodes(G, pos, ax=ax, node_size=900)
    nx.draw_networkx_labels(G, pos, ax=ax)

    curved_edges = [edge for edge in G.edges()]
    nx.draw_networkx_edges(G, pos, edgelist=curved_edges, connectionstyle='arc3, rad=0.25', arrows=True, arrowsize=20, node_size=900)
    plt.title(title)
    plt.show()


def dfs(G: nx.DiGraph, source, seen: dict, cycle: list):
    """
    fonction réalisant un parcours en profondeur d'un graphe et permet de récupérer la présence d'un cycle
    :param G: graphe networkx.DiGraph
    :param source: noeud source du parcours
    :param seen: dictionnaire d'état visité ou non
    :param cycle: liste étant les noeuds d'un cycle
    :return: présence d'un cycle ou non
    """
    seen[source] = True
    if G.out_degree(source) == 0 and G.in_degree(source) > 0:
        return True
    for node in G.neighbors(source):

        if node in cycle:
            return False
        elif not seen[node]:
            if dfs(G, node, seen, cycle):
                return True
    return False


def loop_get_cycles(G: nx.DiGraph):
    """
    Fonction permettant de récupérer TOUS les cycles d'un graphe donné, en réalisant un parcours en profondeur depuis
    chaques noeuds non parcourus
    :param G: Graphe networkx.Digraph
    :return: liste de liste de noeuds représentant la liste des cycles du graphe
    """
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
    """
    parcours en profondeur permettant de récupérer les noeuds d'un potentiel cycle
    :param G: graphe networkx.DiGraph
    :param source: noeud source (player)
    :param seen: dictionnaire d'état parcouru ou non
    :param current_path: chemin actuel du parcours en profondeur
    :param id_dict: dictionnaire d'id dans le chemin
    :return: liste de noeuds représentant un unique cycle
    """
    seen[source] = True
    current_path.append(source)
    id_dict[source] = len(current_path)-1
    for node in G.neighbors(source):
        if not seen[node]:
            temp = get_cycles(G, node, seen, current_path, id_dict)
            if len(temp) > 0:
                print(temp)
                return temp
        elif id_dict[node] > -1:
            return current_path[id_dict[node]:]
    current_path.pop(-1)
    id_dict[source] = -1
    return []


def pull_max_pref(player, label):
    """
    étant donné un joueur et un profil de stratégie, on récupère le meilleur choix de chemins pour le joueur
    :param player: joueur de typle Player
    :param label: str d'une stratégie
    :return: la meilleur stratégie en réponse
    """
    max_pref = None
    for strategy in player.preference:
        if label in strategy.strategy:
            if max_pref is None or player.preference[max_pref] < player.preference[strategy]:
                max_pref = strategy
    return max_pref


def stuck_in_cycle(G: nx.DiGraph, cycle: list, player):
    """
    fonction permettant de détecter si un joueur est bloqué dans un cycle ou non, si un chemin direct est moins bien
    qu'un chemin indirect
    :param G: Graphe de jeu networkx.DigGraph
    :param cycle: cycle à évaluer pour savoir si on reste bloqué à l'intérieur
    :param player: joueur de départ
    :return: bool
    """
    d = {p[2]: p[:2] for p in G.edges.data(nbunch=player, data="w", default="")}
    max_out, max_in = 0, 0
    max_out_path = None

    for label in d:
        #print(label, player)
        path = pull_max_pref(player, label)
        #print(label, player)
        if path is not None:
            if d[label][1] in cycle:
                if player.preference[path] > max_in:
                    max_in = player.preference[path]
            else:
                if player.preference[path] > max_out:
                    max_out = player.preference[path]
                    max_out_path = path
    return max_in > max_out, max_out_path

def get_edges_from_name(edges_name: set[str], G: nx.DiGraph):
    """
    fonciton permettant de récupérer un set d'arcs(tuple) à partir d'un set de nom des arrêtes(str)
    :param edges_name: set des noms des arrêtes
    :param G: graphe de jeu networkx.Digraph
    :return: set[tuple] d'arcs correspondant
    """
    edges = set()
    for edge in G.edges():
        if G.get_edge_data(*edge)["w"] in edges_name:
            edges.add(edge)
            if len(edges) == len(edges_name):
                return edges
    return edges


def same_end(path_intersection: set[tuple]):
    """
    étant donné l'intersection de 2 chemins on regarde si cela forme un chemin vers la fin
    :param path_intersection: set d'arcs étant l'intersection de 2 chemins
    :return:
    """
    i, count = 0, 0
    current = "vb"
    while i < len(path_intersection):
        in_lst = [tpl for tpl in path_intersection if tpl[1].name == current]
        if len(in_lst) == 0:
            return False
        current = in_lst[0][0]
        i += 1
    return True


def is_sdw(lst_path_out: list, G: nx.DiGraph):
    """
    heuristique pour déterminer si une certaine DW est une SDW (ne fonctionne pas dans 100% des cas)
    :param lst_path_out: chemin sortant depuis un noeud du cycle
    :param G: graphe de jeu networkx.DiGraph
    :return: bool
    """
    for path_source in lst_path_out:
        for path_target in lst_path_out:
            #print(path_source, path_target)
            if 0 < len(path_source.strategy.intersection(path_target.strategy)) < len(path_source.strategy):
                path_s_temp = get_edges_from_name(path_source.strategy, G)
                path_t_temp = get_edges_from_name(path_target.strategy, G)
                if not same_end(path_s_temp.intersection(path_t_temp)):
                    return False
    return True


def find_dw_sdw(G: nx.DiGraph):
    """heuristique pour déterminer la présence d'une DW et si jamsi d'une SDW, ne fonctionne pas dans tous les cas,
    seulement un cas particulier"""
    cycles = loop_get_cycles(G)
    for cycle in cycles:
        lst_path_out = []
        dw = True
        for player in cycle:
            is_stuck, path_out = stuck_in_cycle(G, cycle, player)
            if path_out is not None:
                lst_path_out.append(path_out)
            if not is_stuck:
                dw = False
                break
        if dw:
            print(lst_path_out)
            return True, is_sdw(lst_path_out, G)
    return False, False


def is_fair_cycle(dyna_G: nx.DiGraph, cycle: list,players:list,nodes_strat):
    """
    fonction permettant de déterminer si un cycle donné en paramètre est équitable ou non, en donnant le graphe de dyna
    , les joueurs, et  nodes_strat
    :param dyna_G: graphe de dynamique networkx.DiGraph
    :param cycle: liste de noeuds du graphe de dynamique
    :param players: liste de joueurs de typle Player
    :param nodes_strat:
    :return: bool
    """
    for strategy in cycle:
        #print(strategy, dyna_G.out_degree(strategy))
        if dyna_G.out_degree(strategy) > 1:
            for strategy_target in list(dyna_G.successors(strategy)):
                if strategy_target not in cycle:
                    for player in players:
                        source_index = nodes_strat[0].index(strategy)
                        source_target = nodes_strat[0].index(strategy_target)
                        if outcome(player,nodes_strat[1][source_index])< outcome(player,nodes_strat[1][source_target]):
                            return False
    return True


def get_nodes_of_dynamic_graph(graph:nx.DiGraph):
    """
    fonciton permettant d'obtenir les profils de stratégie sous forme de sets et de liste de string pour avoir un
    meilleur affichage (obtient les profils de stratégie)
    :param graph: graphe de jeu
    :return:
    """
    nodes = []
    set_of_edges_label = set()
    my_list = []
    node_label_content = []
    strategy_profiles = list(map(set,get_strategy_profiles(graph)))
    for strategy_profile in strategy_profiles:
        for player_strategy in strategy_profile:
            temp = graph.get_edge_data(*player_strategy)["w"]
            node_label_content.append(temp)
            set_of_edges_label.add(temp)
        nodes.append(''.join(node_label_content))
        my_list.append(set_of_edges_label)
        node_label_content = []
        set_of_edges_label = set()
    return nodes,my_list,list(map(set,(strategy_profiles)))


def get_edges_from_path(path:list):
    """
    fonciton qui à partir d'une liste de noeud permet de récupérer les arcs entre les noeuds(dans l'ordre de la liste)
    :param path: liste de noeud formant un chemin
    :return: set d'arcs
    """
    set_edges = set()
    for i in range(len(path)-1):
        set_edges.add((path[i],path[i+1]))
    return set_edges


def is_n1tg(G:nx.DiGraph):
    """
    fonction permettant de savori si un jeu fournis dans une classe Game est un N1TG ou non permettant d'en savoir plus
    :param G: graphe de jeu
    :return: bool
    """
    players = list(filter(lambda x: (G.out_degree[x] > 0), G.nodes))
    vBot = list(filter(lambda x: (G.out_degree[x] == 0), G.nodes))
    for player in players:
        player_permitted_paths = list(nx.all_simple_paths(G,player,*vBot))
        for path1 in player_permitted_paths:
            for path2 in player_permitted_paths:
                if path1 != path2:
                    if path1[1] == path2[1]:
                        edges = [get_edges_from_path(path1),get_edges_from_path(path2)]
                        strategies = [get_edge_name_set(edges[0],G),get_edge_name_set(edges[1],G)]
                        if outcome(player,strategies[0]) != outcome(player,strategies[1]):
                            return False
    return True



# fonctions utiles:
#get_edges_from_path(path)
#get_edge_name_set(edge,G)
#





