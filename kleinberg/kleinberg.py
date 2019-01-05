import networkx as nx
import matplotlib.pyplot as plt


file_name = "../tech-routers-rf.mtx"
data = open(file_name, 'r')

u = []
pos = []
x = 0
y = 0
increment = 1
init = True

for line in data:
	if init:
		init = False
		continue
	nodes = []
	nodes = line.split()
	nodes[0] = int(nodes[0])
	nodes[1] = int(nodes[1])

	u.append((nodes[0], { 'pos': (x, y) }))

	if x < 47*increment:
		x += increment
	else:
		x = 0
		y += increment

for node in u:
	pos.append(node[1]['pos'])

G = nx.Graph()
name = "kleinberg.pdf"

node_list = []
labels = {}

for node in u:
	labels[node[0]] = str(node[0])
	node_list.append(node[0])

nx.draw_networkx_nodes(G, pos,
						nodelist=node_list,
						node_color="r",
						node_size=10,
						alpha=0.9)
nx.draw_networkx_labels(G, pos, labels, font_size=1.5)
plt.savefig(name, format="PDF")
G.clear
