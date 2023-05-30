from util import *
import networkx as nx

G = nx.DiGraph()

G.add_node(1)
G.add_node(2)
G.add_node(3)

edge_list = [(1,2,{"w": "c1"}),(2,1,{"w": "c2"}),(1,3,{"w": "s1"}),(2,3,{"w": "s2"})]
G.add_edges_from(edge_list)

preferences = {1: [{(1,2), (2,1)}, {(1,3)}, {(1,2),(2,3)}],
               2: [{(2,1), (1,2)}, {(2,3)}, {(2,1),(1,3)}]}




affichage(G)

"""dyna_P1 = nx.DiGraph()
all_neighbors = [G.neighbors(n) for n in G.nodes()]
for i in range(len(all_neighbors)):
    neighbors = all_neighbors[i]
"""
nodes = list(G.nodes())
nodes.sort(key=lambda x: len(list(G.neighbors(x))))
nodes = nodes[1:]
print(nodes)

"""def const_chemins_old(G: nx.DiGraph, nodes, i):
    if i < len(nodes):
        res = []
        for n in G.neighbors(nodes[i]):
            temp = const_chemins(G, nodes, i+1)
            if not temp:
                res.append([(nodes[i],n)])
            else:
                for ch in temp:
                    res.append([(nodes[i],n)] + ch)

        return res
    return []"""


def const_chemins(G: nx.DiGraph, nodes, i):
    """
    fonction déterminant les stratégie possibles pour le jeu donnée, spécialisé pour P1
    :param G: graphe à utiliser
    :param nodes: noeuds du graphe triés par ordre de degré
    :param i: indice du noeud dans la liste
    :return: liste de sets de chaques stratégie
    """
    if i < len(nodes):
        res = []
        for n in G.neighbors(nodes[i]):
            temp = const_chemins(G, nodes, i+1)
            if not temp:
                res.append({(nodes[i], n)})
            else:
                for ch in temp:
                    ch.add((nodes[i], n))
                    res.append(ch)

        return res
    return []


chemins_dyna = const_chemins(G, nodes, 0)
print(chemins_dyna)



def gain(preferences: dict, strategy: set, key):
    """
    calcul du gain pour la stratégie donnée en fonction de la préférence du joueur donnée (key)
    :param preferences: préférences de tous les joueurs
    :param strategy: la strategy dont on veut savoir l'outcome
    :param key: l'indice du joueur
    :return: int: outcome de la stratégie
    """
    for j in range(len(preferences[key])):
        pref = preferences[key][j]
        if pref.issubset(strategy):
            return j
    return 0


for i in preferences.keys():
    print(f'gains joueur {i}:')
    for ch in chemins_dyna:
        print(ch, gain(preferences, ch, i))


def const_dyna_graph_P1(preferences: dict, chemins_dyna : list[set]):
    dyna_P1 = nx.DiGraph()
    for i in range(len(chemins_dyna)):
        strategy1 = chemins_dyna[i]
        for j in range(len(chemins_dyna)):
            strategy2 = chemins_dyna[j]
            difference = strategy1.difference(strategy2)
            #print(difference)
            if len(difference) == 1:
                node = difference.pop()
                if gain(preferences, strategy1, node[0]) < gain(preferences, strategy2, node[0]):
                    dyna_P1.add_edge(i, j)
    return dyna_P1


dyna_P1 = const_dyna_graph_P1(preferences, chemins_dyna)
affichage_dyna(dyna_P1)


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

print(loop_cycle_detection(dyna_P1))

#TODO: tester la fonction et l'adapter dans le style de Bill-kelly (mauvais stockage des stratégies et de méthode)
def const_dyna_graph_bestP1(preferences: dict, chemins_dyna : list[set]):
    """
    fonction mémorisant la meilleur réponse pour chaques stratégie et chaques joueur pour savoir
    où mettre des arcs dans le graphe
    :param preferences: chemins préférés des joueurs
    :param chemins_dyna: noeuds du graphe de dynamiques qui sont des routes
    :return: le grapeh de la dynamique bP1
    """
    dyna_bP1 = nx.DiGraph()
    for i in range(len(chemins_dyna)):
        strategy1 = chemins_dyna[i]
        best_reply = {n: None for n in G.nodes()}
        for j in range(len(chemins_dyna)):
            strategy2 = chemins_dyna[j]
            difference = strategy1.difference(strategy2)

            if len(difference) == 1:
                node = difference.pop()

                if gain(preferences, strategy1, node[0]) < gain(preferences, strategy2, node[0]):
                    if best_reply[node[0]] is None or gain(preferences, strategy2, node[0]) > gain(preferences, chemins_dyna[best_reply[node[0]]], node[0]):
                        best_reply[node[0]] = j

        for reply in best_reply.values():
            if reply is not None:
                dyna_bP1.add_edge(i, reply)
    return dyna_bP1


dyna_bP1 = const_dyna_graph_bestP1(preferences, chemins_dyna)
affichage_dyna(dyna_bP1)

def const_dyna_graph_PC(preferences: dict, chemins_dyna : list[set]):
    dyna_PC = nx.DiGraph()
    for i in range(len(chemins_dyna)):
        strategy1 = chemins_dyna[i]
        for j in range(len(chemins_dyna)):
            strategy2 = chemins_dyna[j]
            difference = strategy1.difference(strategy2)
            difference2 = strategy2.difference(strategy1)
            #print(difference)
            if len(difference) > 0:
                count = 0
                for edge1 in difference:
                    for edge2 in difference2:
                        if edge2[0] == edge1[0]:
                            temp = strategy1.copy()
                            temp.discard(edge1)
                            temp.add(edge2)
                            break
                    if gain(preferences, strategy1, edge1[0]) <= gain(preferences, temp, edge1[0]):
                        count += 1
                if count == len(difference):
                    dyna_PC.add_edge(i, j)
    return dyna_PC

dyna_PC = const_dyna_graph_PC(preferences, chemins_dyna)
affichage_dyna(dyna_PC)

def const_dyna_graph_bestPC(preferences: dict, chemins_dyna : list[set]):
    dyna_bPC = nx.DiGraph()
    for i in range(len(chemins_dyna)):
        strategy1 = chemins_dyna[i]
        best_reply = {n: None for n in G.nodes()}
        for j in range(len(chemins_dyna)):
            strategy2 = chemins_dyna[j]
            difference = strategy1.difference(strategy2)
            difference2 = strategy2.difference(strategy1)
            #print(difference)
            if len(difference) > 0:
                count = 0
                for edge1 in difference:
                    for edge2 in difference2:
                        if edge2[0] == edge1[0]:
                            temp = strategy1.copy()
                            temp.discard(edge1)
                            temp.add(edge2)
                            break
                    if gain(preferences, strategy1, edge1[0]) <= gain(preferences, temp, edge1[0]):
                        if best_reply[edge1[0]] is None or gain(preferences, temp, edge1[0]) > gain(preferences, best_reply[edge1[0]][1], edge1[0]):
                            best_reply[edge1[0]] = (j,temp)
                        count += 1
                for reply in best_reply.values():
                    if reply is not None:
                        dyna_bPC.add_edge(i, reply[0])
    return dyna_bPC


dyna_bPC = const_dyna_graph_bestPC(preferences, chemins_dyna)
affichage_dyna(dyna_bPC)