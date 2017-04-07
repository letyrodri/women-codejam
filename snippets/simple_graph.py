class Graph:

    adj_list = []
    w = []
    node_qty = 0

    def __init__(self, node_qty):
        self.adj_list = [[] for x in range(0, node_qty+1)]
        self.node_qty = node_qty
        self.w = [[0 for y in range(0, self.node_qty+1)] for x in range(0, self.node_qty+1)]


    def add_edge(self, node1, node2, weight):
        self.adj_list[node1].append(node2)
        self.w[node1][node2] = weight


