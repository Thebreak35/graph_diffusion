import networkx as nx
import matplotlib.pyplot as plt
from random import randint

def rnd():
	return randint(0,9)

G = nx.DiGraph()
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

# print(e[0][2]['weight'])

direct_e = {1:[4, 6, 7],
			2:[1, 3],
			3:[],
			4:[2, 3, 5],
			5:[9],
			6:[4, 5],
			7:[6, 8],
			8:[],
			9:[6, 8]}

w = [0.3, 0.2, 0.4,
	 0.4, 0.4,
	 0.2, 0.3, 0.4,
	 0.4,
	 0.3, 0.2,
	 0.3, 0.2,
	 0.3, 0.3]

sum_th = [0, 0, 0, 0, 0, 0, 0, 0, 0]
activate_th = [0, 0.8, 0.6, 0.5, 0.6, 0, 0.5, 0.4, 0.4]
activate_set = [1,6]
activate_used = []

for i in activate_set:
	if i in activate_used:
		continue
	for l in e:
		if l[0] == i:
			u1 = l[0]
			u2 = l[1]
			u_w = float(l[2]['weight'])
			sum_th[u2 - 1] += u_w
			if sum_th[u2 - 1] >= activate_th[u2 - 1]:
				if u2 not in activate_set:
					activate_set.append(u2)
			print('u : ', u1, ' v : ', u2, ' w : ',u_w ,' sum_th : ', sum_th)
	activate_used.append(i)

activate_set.sort()
print(activate_set)

G.add_edges_from(e)

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
plt.savefig("path.png", format="PNG")