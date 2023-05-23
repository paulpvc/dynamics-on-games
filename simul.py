import networkx as nx
import matplotlib.pyplot as plt
import my_networkx as my_nx


def init():
    G = nx.DiGraph()
    nb_noeud = int(input("nombre de noeuds: "))
    for i in range(nb_noeud):
        label = input(f"label du noeud {i+1}: ")
        G.add_node(label)
    nb_arcs = int(input("nombre d'arcs"))
    print("arc: source destination label")
    for i in range(nb_arcs):
        source, dest, label = input(f"arc {i+1}: ").split()
        G.add_edges_from([(source, dest, {"w": label})])
    M_aj = nx.adjacency_matrix(G)



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

init()