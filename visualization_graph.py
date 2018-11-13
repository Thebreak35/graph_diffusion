import networkx as nx
import matplotlib.pyplot as plt
# import scipy.io as scipy
from random import uniform
import pprint as pp


def rnd():
	return uniform(0, 1000000)

def isInfect(prob):
	if uniform(0, 1) < prob:
		return True
	return False

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

file_name = "tech-routers-rf.mtx"
data = open(file_name, 'r')

u = []
u_appended = []
pos = []
e = []
activate_set = [1920, 136, 754, 582, 630, 1489, 1119, 1712]
activate_used = []

not_included = 0
for line in data:
	if not_included < 2:
		not_included += 1
		continue
	nodes = line.split()
	nodes[0] = int(nodes[0])
	nodes[1] = int(nodes[1])

	if nodes[0] not in u_appended:
		u.append((nodes[0], { 'pos': (rnd(), rnd()) }))
		u_appended.append(nodes[0])

	if nodes[1] not in u_appended:
		u.append((nodes[1], { 'pos': (rnd(), rnd()) }))
		u_appended.append(nodes[1])

	edge = (nodes[0], nodes[1], {'weight': uniform(0, 1)})
	e.append(edge)

pos.append((0,0)) # node1 doesn't exist

u.sort()
e.sort()

for node in u:
	pos.append(node[1]['pos'])

printGraph("independent_large_before", True)
print('act: ', activate_set)
for i in activate_set:
	if i in activate_used:
		continue
	for edge in e:
		if edge[0] == i:
			u1 = edge[0]
			u2 = edge[1]
			u_w = float(edge[2]['weight'])
			if isInfect(u_w) and u2 not in activate_set:
				activate_set.append(u2)
	activate_used.append(i)
print('act: ',activate_set)
printGraph("independent_large_after", False)