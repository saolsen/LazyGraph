# -*- coding: utf-8 -*-
"""
    LazyGraph
    ---------
    A lazy graph processing library for python.

    :copyright: (c) 2011 by Stephen Olsen.
    :license: MIT, see LICENSE for more details.

    This is a collection of functions that work on graphs that were created by
    subclassing BaseNode or made with the NodeBuilder. The plan is to eventually
    have just about every common graph processing function in here working on
    lazy graphs.
"""

__author__ = 'Stephen Olsen'

from collections import deque

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
