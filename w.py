
import matplotlib.pyplot as plt
import networkx as nx

G = nx.DiGraph()

G.add_edge('Read Image','222222222222')
G.add_edge('Read Image','333333333333')
G.add_edge('333333333333','222222222222')
G.add_edge('333333333333','444444444444')
G.add_edge('444444444444','333333333333')

nx.draw(G, with_labels=True, node_size=10000, node_color='cyan', edgecolors='k', width=2.0)
plt.show()