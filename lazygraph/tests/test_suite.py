# -*- coding: utf-8 -*-
"""
    LazyGraph
    ---------
    A lazy graph processing library for python.

    :copyright: (c) 2011 by Stephen Olsen.
    :license: MIT, see LICENSE for more details.
"""

__author__='Stephen Olsen'

import os, sys
cmd_folder = os.path.dirname(os.path.abspath('../'))
if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)

import unittest
import lazygraph.basenode as basenode
import lazygraph.functions as f

simple_graph = {'a':['b','c'],'b':['d','a'],'c':['b'],'d':['e'],'e':['c']}

# A simple class overload to test
class TestNode(basenode.BaseNode):
    def _get_edges(self):
        self._edges = simple_graph[self._id]

class TestBaseNodeClass(unittest.TestCase):
    def test_FirstTest(self):
        path = f.BFS_findPath('a', 'e', TestNode)
        self.assertEqual(path, ['a','b','d','e'])

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestBaseNodeClass)
    unittest.TextTestRunner(verbosity=2).run(suite)
