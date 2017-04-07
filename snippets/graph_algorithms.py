# Dijkstra Shortest-Path - Implementation Cormen's Book Pseudocode

# Input: G = Graph Adyacency List in a List(List())
#		 w = lisf of list - edge weights
#		 s = Starting node

# Shortest path from one node to the rest
# Positive Weighted Graph

def dijkstra(G, w, s):
	d = []  # distances array
	p = []  # parents array

	for v in range(0,len(G)):
		d.append(float("Inf"))
		p.append(None)

	# the distance for starting node is the same
	d[s] = 0

	S = set()
	Q = [( d[x], x ) for x in range(1,len(G)) ]

	while (Q):
		e = min(Q)
		u = e[1]
		Q.remove(e)

		# iterates u adyacents
		for v in G[u]:
			if d[v] > d[u]+w[u][v]:
				Q.remove((d[v],v))
				d[v] = d[u]+w[u][v]
				p[v] = u
				Q.append( (d[v],v))

	return d, p

def get_path(p,s,e):
	node = e
	res = []

	while (not node == s):
		res.append(node)
		node = p[node]

	res.append(s)
	res.reverse()

	return res