import networkx as nx
import matplotlib.pyplot as plt
# from scipy import special, optimize, io as sp

rawfile = open('tech-RL-caida.mtx', 'r')
i = 0
max_u = 0
max_v = 0
max_e = 0
G = nx.Graph()
for line in rawfile:
	if (i == 0):
		i = 1
	elif (i == 1):
		i = 2
		arr = line.split()
		max_u = int(arr[0])
		max_v = int(arr[1])
		max_e = int(arr[2])
		for n in range(1, max_v + 1):
			G.add_node(n)
			# print(n)
	else:
		arr = line.split()
		print(arr)
		G.add_edge(int(arr[0]), int(arr[1]))
H = nx.Graph(G)
nx.draw(H, with_labels=True)
plt.savefig("path.png")