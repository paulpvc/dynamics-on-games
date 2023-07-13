import networkx as nx

date = 0


def visit_node_in_dfs(node, G:nx.DiGraph, color: dict,visited: list, discovery_date:dict, treatment_end_date:dict,back_edges:set,forward_and_cross_edges:set,liaison,cycles):
  color[node] = "g"
  global date
  date+=1
  discovery_date[node] = date
  for successor in list(G.successors(node)):
      if color[successor] == "w":
          visited.append(successor)
          liaison.add((node,successor))
          visit_node_in_dfs(successor,G,color,visited,discovery_date,treatment_end_date,back_edges,forward_and_cross_edges,liaison,cycles)
      elif color[successor] == "g":
          back_edges.add((node,successor))
          cycles.append(visited[visited.index(successor):visited.index(node)+1])

          
      if  color[successor] == "b" and (node,successor) not in liaison:
          forward_and_cross_edges.add((node,successor))
  color[node] = "b"
  date+=1
  treatment_end_date[node] = date



def depth_first_search(G:nx.DiGraph):
    color = {node: "w" for node in list(G.nodes())}
    visited = []
    discovery_date = {}
    treatment_end_date = {}
    forward_and_cross_edges = set()
    liaison = set()
    back_edges = set()
    cycles = []
    global date
    date = 0
    for node in list(G.nodes()):
        visited = [node]
        if color[node] == "w":
            visit_node_in_dfs(node,G,color,visited,discovery_date, treatment_end_date,back_edges,forward_and_cross_edges,liaison,cycles)

    #print(forward_and_cross_edges)

    return {"cycles":cycles,
            "discovery_date":discovery_date,
            "treatment_end_date":treatment_end_date,
            "back_edges":back_edges,
            "forward_and_cross_edges": forward_and_cross_edges,
            "liaison": liaison
            }

def contains_cycle(G:nx.DiGraph):
    return len(depth_first_search(G)["back_edges"]) > 0

def get_cycles(G:nx.DiGraph):
    pass



def topological_sorting (G:nx.DiGraph):
    treatment_end_date = depth_first_search(G)["treatment_end_date"]
    list_nodes = []
    for node in treatment_end_date:
        list_nodes.append(node)
    return list_nodes


def visit_node_in_dfs_for_kosaraju(node,G: nx.DiGraph,visited:dict,color:dict,component,liaison,forward_and_cross_edges):
    color[node] = "g"
    for successor in list(G.successors(node)):
        if color[successor] == "w":
            liaison.add((node, successor))
            component.append(successor)
            visited[node] = successor
            visit_node_in_dfs_for_kosaraju(successor, G,visited,color,component,liaison, forward_and_cross_edges)
        if color[successor] == "b" and (node, successor) not in liaison:
            forward_and_cross_edges.add((successor,node))
    color[node] = "b"

def depth_first_search_for_kosaraju(G:nx.DiGraph, treatment_end_date:dict):
    color = {node: "w" for node in list(G.nodes())}
    visited = {node: None for node in list(G.nodes)}
    connected_components = {}
    id = 0
    liaison = set()
    forward_and_cross_edges = set()
    sorted_desc_treatment_end_date = dict(sorted(treatment_end_date.items(),key=lambda item: item[1],reverse=True))
    #print(sorted_desc_treatment_end_date)
    for node in sorted_desc_treatment_end_date:
        if color[node] == "w":
            component = [node]
            id+=1
            visit_node_in_dfs_for_kosaraju(node,G,visited,color,component,liaison,forward_and_cross_edges)
            connected_components[id] = component
            #print(component)
            #print(forward_and_cross_edges)
    return [connected_components, forward_and_cross_edges]


def kokosaraju(G:nx.DiGraph):
    infos = depth_first_search(G)
    treatment_end_date = infos["treatment_end_date"]
    forward_and_cross_edges = infos["forward_and_cross_edges"]
    #print(treatment_end_date)
    transpose = G.reverse()
    #print(transpose)
    return depth_first_search_for_kosaraju(transpose,treatment_end_date)


def get_connected_components_graph(G:nx.DiGraph):
    connected_components_graph = nx.DiGraph()
    connected_components,edges = kokosaraju(G)
    #print(connected_components)
    connected_components_graph.add_nodes_from(list(connected_components.keys()))
    new_edges = []
    for i in connected_components.keys():
        for j in connected_components.keys():
            if i == j:
                continue
            for node in connected_components[i]:
                for node2 in connected_components[j]:
                    if (node,node2) in edges and (node, node2) not in new_edges:
                        new_edges.append((i,j))
        connected_components_graph.add_edges_from(new_edges)
    return [connected_components_graph, connected_components]


def score(G:nx.DiGraph):
    score = {}
    temp_score = {}
    connected_component_graph, connected_components = get_connected_components_graph(G)
    list = topological_sorting(connected_component_graph)
    for id in connected_components:
        temp_score[id] = len(list)-list.index(id)
        for el in connected_components[id]:
            score[el] = temp_score[id]
    return score



"""
color = {}

nodes = [1, 2, 3, 4, 5, 6, 7, ]
edges = [(1, 2), (2, 3), (3, 4), (4, 1), (2, 5), (5, 6), (6, 5), (5, 7), (3, 5)]
G = get_graph(nodes, edges)

#c = {(2, 5): "polo"}
#print(c[(2, 5)])
#print(depth_first_search(G.reverse()))

#print(get_connected_components_graph(G))
#print(topological_sorting(get_connected_components_graph(G)[0]))
print(G.out_degree(5), "eédu")
    # affichage_dyna(get_connected_components_graph(G),"composante")

"""