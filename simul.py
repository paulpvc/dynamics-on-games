import networkx as nx
import matplotlib.pyplot as plt
import my_networkx as my_nx


def init():
    G = nx.DiGraph()
    G.add_node("v1")
    G.add_node("v2")
    G.add_node("vB")
    edge_list = [("v1", "v2", {"w": "c1"}), ("v2", "v1", {"w": "c2"}), ("v1", "vB", {"w": "s1"}), ("v2", "vB", {"w": "s2"})]
    G.add_edges_from(edge_list)

    """nb_noeud = int(input("nombre de noeuds: "))
    for i in range(nb_noeud):
        label = input(f"label du noeud {i+1}: ")
        G.add_node(label)
    nb_arcs = int(input("nombre d'arcs"))
    print("arc: source destination label")
    for i in range(nb_arcs):
        source, dest, label = input(f"arc {i+1}: ").split()
        G.add_edges_from([(source, dest, {"w": label})])"""
    M_aj = nx.adjacency_matrix(G)
    affichage(G)


def affichage(G):
    pos = nx.spring_layout(G, seed=5)
    fig, ax = plt.subplots()
    nx.draw_networkx_nodes(G, pos, ax=ax)
    nx.draw_networkx_labels(G, pos, ax=ax)

    curved_edges = [edge for edge in G.edges()]
    nx.draw_networkx_edges(G, pos, edgelist=curved_edges, connectionstyle='arc3, rad=0.25')
    edge_weights = nx.get_edge_attributes(G, 'w')
   # curved_edge_labels = {edge: edge_weights[edge] for edge in curved_edges}
    #my_nx.my_draw_networkx_edge_labels(G, pos, ax=ax, edge_labels=curved_edge_labels, rotate=False, rad=0.25)
    plt.show()




def is_edge(node1, node2,pref,i):
    if node1[0+i:2+i]!=node2[0+i:2+i] and pref.index(node1)<pref.index(node2) and  node1[2-i:4-i]==node2[2-i:4-i]:
        return True
    else:
        return False

strategies = ["c1c2", "c1s2", "s1c2", "s1s2"]
pref_1 = ["c1c2","s1c2","s1s2","c1s2"]
pref_2 = ["c1c2","c1s2", "s1s2","s1c2"]

dynamic_graph = nx.DiGraph()
dynamic_graph.add_nodes_from(strategies)
for node1 in strategies:
    for node2 in strategies:
        if(is_edge(node1,node2,pref_1,0)):
            dynamic_graph.add_edge(node1,node2)
for node1 in strategies:
    for node2 in strategies:
        if(is_edge(node1,node2,pref_2,2)):
            dynamic_graph.add_edge(node1,node2)



affichage(dynamic_graph)