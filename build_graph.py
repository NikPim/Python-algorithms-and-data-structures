class Graph:
    def __init__(self):
        self.number_of_nodes = 0
        self.adjacent_list = {}
        
    def add_node(self, node):
        self.adjacent_list[node] = []
        self.number_of_nodes += 1

    def add_edge(self, node1, node2):
        self.adjacent_list[node1].append(node2)
        self.adjacent_list[node2].append(node1)

    def represent_graph(self):
        for i, nodes in self.adjacent_list.items():
            print(i, nodes)

myGraph = Graph()
myGraph.add_node('0')
myGraph.add_node('1')
myGraph.add_node('2')
myGraph.add_node('3')
myGraph.add_node('4')
myGraph.add_node('5')
myGraph.add_node('6')
myGraph.add_edge('3', '1')
myGraph.add_edge('3', '4')
myGraph.add_edge('4', '2')
myGraph.add_edge('4', '5')
myGraph.add_edge('1', '2')
myGraph.add_edge('1', '0')
myGraph.add_edge('0', '2')
myGraph.add_edge('6', '5')

print(myGraph.represent_graph())