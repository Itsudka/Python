import networkx as nx
import matplotlib.pyplot as plt

reglas = [
    ("A", "B", 5),  
    ("B", "C", 3),  
    ("C", "D", 2),  
    ("D", "E", 4),  
    ("E", "F", 1),  
    ("A", "C", 7),  
    ("C", "F", 6),  
]

G = nx.Graph()
for origen, destino, distancia in reglas:
    G.add_edge(origen, destino, weight=distancia)

punto_A = "A"
punto_B = "F"

ruta = nx.dijkstra_path(G, punto_A, punto_B)

print("Ruta más corta:", ruta)

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color="lightblue")
labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.show()