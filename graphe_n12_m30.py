import networkx as nx
import matplotlib.pyplot as plt
import random

def random_graph(n, m):
    edges = set()
    while len(edges) < m:
        u = random.randint(1, n)
        v = random.randint(1, n)
        if u != v:
            edges.add((min(u, v), max(u, v)))
    return list(edges)

def welsh_powell_coloring(n, conflicts):
    
    G = nx.Graph()
    G.add_nodes_from(range(1, n + 1)) 
    G.add_edges_from(conflicts)        

    sorted_nodes = sorted(G.degree, key=lambda x: x[1], reverse=True)
    nodes_order = [node for node, _ in sorted_nodes]

    coloring = {}
    for node in nodes_order:

        neighbor_colors = {coloring[neighbor] for neighbor in G.neighbors(node) if neighbor in coloring}

        for color in range(1, n + 1):  
            if color not in neighbor_colors:
                coloring[node] = color
                break

    return coloring

def draw_colored_graph(n, conflicts, coloring):

    G = nx.Graph()
    G.add_nodes_from(range(1, n + 1))  
    G.add_edges_from(conflicts)      

    colors = [coloring[node] for node in G.nodes]

    pos = nx.spring_layout(G) 
    plt.figure(figsize=(8, 6))
    nx.draw(
        G, pos, with_labels=True, node_color=colors, node_size=800, cmap=plt.cm.rainbow
    )
    plt.title("Graphe Coloré des Matières (Créneaux)")
    plt.show()

n = 12 
m = 30  
conflicts = random_graph(n, m)

coloring = welsh_powell_coloring(n, conflicts)

print("Créneaux attribués aux matières :")
for subject, slot in sorted(coloring.items()):
    print(f"Matière {subject} : Créneau {slot}")

print(f"Nombre total de créneaux utilisés : {max(coloring.values())}")

draw_colored_graph(n, conflicts, coloring)
