# -*- coding: utf-8 -*-
"""
    LazyGraph
    ---------
    A lazy graph processing library for python.

    :copyright: (c) 2011 by Stephen Olsen.
    :license: BSD, see LICENSE for more details.
"""

__version__='0.0.1'
__author__='Stephen Olsen'

class BaseNode(object):
    """
    This is the base Node object for defining graphs to be evaluated with the
    lazygraph library.
    The way thay you create graphs in lazygraph is by defining how a node
    gets it's data. When you create a Node, all you do is pass in it's id, this
    way only the id is stored in memory until the node is ready to be processed
    and then at that time any other necessary information will be loaded.
    To accomplish this we don't specify what the data and edges for the node are
    when we create a node instance but instead we specify how to get the data
    we need at runtime from the node id.
    """
    def __init__(self, _id):
        """
        When an instance of the node is created, the only thing it has is an id
        Edges and Data will be loaded later when we need them. You may also
        add in things like a database connection.
        """
        self._edges = None
        self._data  = None
        self._id    = _id
        # self._dbConnect = SomeAlreadySpecifiedConnection
        
    def edges(self):
        """
        The edges are returned if they have already been loaded, otherwise they
        are loaded using the _get_edges() function (this is a user specified
        function that gets the edges)
        """
        if (self._edges):
            return self._edges
        else:
            self._get_edges()
            return self._edges

    def data(self):
        """
        Data is another thing that we don't load untill we need it. It isn't
        necessary to have data for your node and none of the functions in
        lazygraph.compute use it but it's built in because many people want it.
        """
        if (self._data):
            return self._data
        else:
            self._get_data()
            return self._data

    def _get_edges(self):
        """
        This is the main function that must be overloaded when subclassing
        BaseNode, for the functions in lazygraph.compute to work it is important
        that this function use self._id to get the edges and set self._edges to a
        list of strings (this list will be the id's for other nodes).
        Other than that how those edges are obtained could be anything (which is
        the whole point of this graph library) They could be as simple as a
        database call, something like
        
            def _get_edges(self):
                # assuming you have set up dbConnect to be a couchdb database connection
                document = self._dbConnect[self._id]
                self._edges =  document.edges
            
        or it can be something more complicated like pulling a webpage and parseing out
        it's links
        TODO: put in an example of that here
        """
        pass
        
    def _get_data(self):
        """
        This is the same deal but the function will use self._id to get the
        'data' of the node which could be anything really. Also if it is simpler
        to get the data and the edges at the same time you can have a function
        called _get_node_data and just call it from both _get_edges and
        _get_data, since it will set both self._data and self._edges the edges
        and data functions should return the info after one call to
        get_node_data()
        """
        pass
    
