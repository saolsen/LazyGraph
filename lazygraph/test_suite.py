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

import unittest
import basenode
import compute

simple_graph = {'a':['b','c'],'b':['d','a'],'c':['b'],'d':['e'],'e':['c']}

# A simple class overload to test
class TestNode(basenode.BaseNode):
    def _get_edges(self):
        self._edges = simple_graph[self._id]

class TestBaseNodeClass(unittest.TestCase):
    def test_FirstTest(self):
        path = compute.BFS_findPath('a', 'e', TestNode)
        self.assertEqual(path, ['a','b','d','e'])

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestBaseNodeClass)
    unittest.TextTestRunner(verbosity=2).run(suite)
