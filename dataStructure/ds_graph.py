

class graph:
    def __init__(self, gdict = None):
        if gdict is None:
            gdict = []
        self.gdict = gdict

    def getVertices(self):
        return list(self.gdict.keys())

    def edges(self):
        return self.findedges()

    def findedges(self):
        edgename = []
        for vertex in self.gdict:
            for nextvertex in self.gdict[vertex]:
                if {nextvertex, vertex} not in edgename:
                    edgename.append({vertex, nextvertex})
        return  edgename

    def addVertex(self, vertex):
        if vertex not in self.gdict:
            self.gdict[vertex] = []

    def AddEdge(self, edge):
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.gdict:
            self.gdict[vertex1].append(vertex2)
        else:
            self.gdict[vertex1] = [vertex2]

graph_elements = {
    "a": ["b", "c"],
    "b": ["a", "d"],
    "c": ["a", "d"],
    "d": ["e"],
    "e": ["d"]
}

g = graph(graph_elements)
print(g.getVertices())
print("\nPrint Edge")
print(g.edges())
print("\nAdd new vertex:")
g.addVertex("f")
print(g.getVertices())
print("\nAdd new Edge")
g.AddEdge({'a', 'e'})
g.AddEdge({'a', 'c'})
print(g.edges())