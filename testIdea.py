#This is just an idea for a graph processing library thats make to run on
#picloud.

from collections import deque
import sys

__author__ = 'Stephen Olsen'

# What I want is a base class that one can override to create a "lazy node"
# Then I'll have a set of graph processing functions that operate on these
# lazy graphs. The typical use case for this would be a very large graph, one
# that you don't want to store in memory but you still want to traverse and do
# other graph processing on. The nodes can be anything really, from data in a
# database to webpages that are parsed to get at the nodes.

# The Node class will be a base class that is overridden but one will look something
# like this

class Node(object):
    def __init__(self, _id):
        self._id = _id
        self._edges = None
        self._data = None

    def edges(self):
        # Keys must be a list of 'id's for other nodes.
        if (self.edges):
            return self.edges
        else:
            self._load_edges()
            return self.edges

    def _load_edges(self):
        pass
        # Does whatever you have to do to load the edges

    def data(self):
        if (self.data):
            return self.data
        else:
            self.load_data()
            return self.data

    def _load_data():
        pass
        # Loads the data however you have too,
        # note: Many times you will load the edges and the data at the same time,
        # in that case just use another function "load_node(self)" and call it
        # the first time you call edges or data

# Then there will be pure graph processing functions that operate on these graphs,
def BFS_findPath(startId, endId, _Class):
    queue = deque([_Class(startId)])
    paths = { startId: [startId] }
    while True:
            node = queue.popleft()
            if node:
                if endId in node.edges():
                    return paths[node._id] + [endId]
                    break
                else:
                    for child in node.edges():
                        if child not in paths:
                            queue.append(_Class(child))
                            paths[child] = paths[node._id] + [child]
            else:
                return "No path exists."
                break

# Now here's a very trivial example of how you would set up a graph,
# Just remember the point is that you don't have to keep the graph
# in memory like this, I'll write better examples soon....
graph_Dict = { 'a': ['b', 'c'], 'b': ['d', 'a'], 'c': ['b'], 'd': ['e'], 'e': ['c'] }

# Set up a class that uses this graph
class DictGraphNode():
    # You typically only need to override load_edges and load_data, in this
    # case we don't have any data associated with our graph.
    def __init__(self, _id):
        self._id = _id
        self._edges = None
        
    def edges(self):
        if (self._edges):
            return self._edges
        else:
            self._load_edges()
            return self._edges

    def _load_edges(self):
        self._edges = graph_Dict[self._id]

# Now we can use the function we defined above to find the path from 'a' to 'e'
def main():
    print BFS_findPath('a', 'e', DictGraphNode)

if __name__=="__main__":
    main()
