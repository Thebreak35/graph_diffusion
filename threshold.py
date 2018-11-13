import networkx as nx
import matplotlib.pyplot as plt
from random import uniform


def rnd():
	return uniform(0.0, 10.0)

def printGraph(name, before):
	name = name + ".png"

	G = nx.Graph()
	G.add_edges_from(e)

	node_list = []
	labels = {}
	for node in u:
		labels[node[0]] = str(node[0])
		if node[0] not in activate_set:
			node_list.append(node[0])

	nx.draw_networkx_nodes(G,pos,
	                       nodelist=activate_set,
	                       node_color="r",
	                       node_size=10,
	                   alpha=0.9)
	nx.draw_networkx_nodes(G,pos,
	                       nodelist=node_list,
	                       node_color='black',
	                       node_size=10,
	                   alpha=0.9)
	if before:
		nx.draw_networkx_edges(G,pos,width=0.1,alpha=0.5,color='grey')
	plt.savefig(name, format="PNG")
	G.clear()
	return


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

printGraph("threshold_before", True)


for i in activate_set:
	if i in activate_used:
		continue
	for edge in e:
		if edge[0] == i:
			u1 = edge[0] # from u
			u2 = edge[1] # to v
			u_w = float(edge[2]['weight'])
			sum_th[u2 - 1] += u_w
			if sum_th[u2 - 1] >= activate_th[u2 - 1]:
				if u2 not in activate_set:
					activate_set.append(u2)
			print('u : ', u1, ' v : ', u2, ' w : ',u_w ,' sum_th : ', sum_th)
			activate_used.append(u1)

activate_set.sort()

printGraph("threshold", False)

