import networkx as nx
import matplotlib.pyplot as plt
from random import uniform


def rnd():
	return uniform(0.0, 10.0)

def infect(prob):
	if uniform(0.0, 1.0) < prob: # with higher prob higher random range
		return True
	return False

u = [(1, {'pos': (rnd(),rnd())}), 
	 (2, {'pos': (rnd(),rnd())}), 
	 (3, {'pos': (rnd(),rnd())}), 
	 (4, {'pos': (rnd(),rnd())}), 
	 (5, {'pos': (rnd(),rnd())}), 
	 (6, {'pos': (rnd(),rnd())}), 
	 (7, {'pos': (rnd(),rnd())}), 
	 (8, {'pos': (rnd(),rnd())}), 
	 (9, {'pos': (rnd(),rnd())})]

pos = [(0,0), (rnd(),rnd()), (rnd(),rnd()), 
		(rnd(),rnd()), (rnd(),rnd()), (rnd(),rnd()),
		(rnd(),rnd()), (rnd(),rnd()), (rnd(),rnd()), (rnd(),rnd())]

e = [(1,4, {'weight': 0.3}), (1,6, {'weight': 0.2}), (1,7, {'weight': 0.4}),
	 (2,1, {'weight': 0.4}), (2,3, {'weight': 0.4}),
	 (4,2, {'weight': 0.2}), (4,3, {'weight': 0.3}), (4,5, {'weight': 0.4}),
	 (5,9, {'weight': 0.4}),
	 (6,4, {'weight': 0.3}), (6,5, {'weight': 0.2}),
	 (7,6, {'weight': 0.3}), (7,8, {'weight': 0.2}),
	 (9,6, {'weight': 0.3}), (9,8, {'weight': 0.3})]

sum_th = [0, 0, 0, 0, 0, 0, 0, 0, 0]
activate_th = [0, 0.8, 0.6, 0.5, 0.6, 0, 0.5, 0.4, 0.4]
activate_set = [1,6]
activate_used = []

G = nx.Graph()

G.add_edges_from(e)

for i in activate_set:
	if i in activate_used:
		continue
	for edge in e:
		if edge[0] == i:
			u1 = edge[0]
			u2 = edge[1]
			u_w = float(edge[2]['weight'])
			if infect(u_w) and u2 not in activate_set:
				activate_set.append(u2)
	activate_used.append(i)


node_list = []
labels = {}
for node in u:
	labels[node[0]] = str(node[0])
	if node[0] not in activate_set:
		node_list.append(node[0])

nx.draw_networkx_nodes(G,pos,
                       nodelist=activate_set,
                       node_color='r',
                       node_size=350,
                   alpha=0.8,
                   with_labels=True)
nx.draw_networkx_nodes(G,pos,
                       nodelist=node_list,
                       node_color='b',
                       node_size=350,
                   alpha=0.8,
                   with_labels=True)
nx.draw_networkx_labels(G,pos,labels,font_size=16)
nx.draw_networkx_edges(G,pos,width=1.0,alpha=0.5)
# G.add_nodes_from(u)
# G.add_edges_from(e)
# pos = nx.get_node_attributes(G,'pos')
# print(pos)
# nx.draw(G, pos, with_labels=True)
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
# plt.show()
plt.savefig("independent.png", format="PNG")