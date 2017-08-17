#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 08:09:20 2017

@author: sss
"""

class Node(object):
    def __init__(self, name):
        '''Assumes name is a string'''
        self.name = name
    def getName(self):
        return self.name
    def __str__(self):
        return self.name

class Edge(object):
    def __init__(self, src, dest):
        '''Assumes src and dest are nodes'''
        self.src = src
        self.dest = dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __str__(self):
        return self.src.getName + '->' + self.dest.getName()

class Digraph(object):
    '''edges is a dict mapping each node to a list of its children'''
    def __init__(self):
        self.edges = {}
    def addNode(self, node):
        if node in self.edges:
            raise ValueError('Duplicate node')
        else:
            self.edges[node] = []
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not (src in self.edges and dest in self.edges):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)
    def childrenOf(self, node):
        return self.edges[node]
    def hasNode(self, node):
        return node in self.edges
    def getNode(self, name):
        for n in self.edges:
            if n.getName() == name:
                return n
        raise NameError(name)
    def __str__(self):
        result = ''
        for src in self.edges:
            for dest in self.edges[src]:
                result = result + src.getName() + '->'\
                         + dest.getName() + ', '
            result += '\n'
        return result[:] #omit final newline


class Graph(Digraph):
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, rev)

B = 'Boston'
P = 'Providence'
N = 'New York'
C = 'Chicago'
D = 'Denver'
Ph = 'Phoenix'
L = 'Los Angeles'

def buildCityGraph(graphType):
    g = graphType()
    for name in (B, P, N, C, D, Ph, L):
        g.addNode(Node(name))
    g.addEdge(Edge(g.getNode(B), g.getNode(P)))
    g.addEdge(Edge(g.getNode(B), g.getNode(N)))
    g.addEdge(Edge(g.getNode(P), g.getNode(B)))
    g.addEdge(Edge(g.getNode(P), g.getNode(N)))
    g.addEdge(Edge(g.getNode(N), g.getNode(C)))
    g.addEdge(Edge(g.getNode(C), g.getNode(D)))
    g.addEdge(Edge(g.getNode(D), g.getNode(Ph)))
    g.addEdge(Edge(g.getNode(D), g.getNode(N)))
    g.addEdge(Edge(g.getNode(L), g.getNode(B)))
    return g

#gg = buildCityGraph(Graph)
#print(gg)

# Exercise 2
nodes = []
nodes.append(Node('ABC'))
nodes.append(Node('ACB'))
nodes.append(Node('BAC'))
nodes.append(Node('BCA'))
nodes.append(Node('CAB'))
nodes.append(Node('CBA'))

g = Graph()
for n in nodes:
    g.addNode(n)

for i in range(len(nodes)):
    for j in range(i+1, len(nodes)):
        diff_count = 0
        for e in range(len(nodes[i].getName())):
            if nodes[i].getName()[e] == nodes[j].getName()[e]:
                continue
            diff_count += 1
            f = nodes[j].getName().index(nodes[i].getName()[e])
            if not abs(e-f) == 1:
                break
        else:
            if diff_count == 2:
                g.addEdge(Edge(nodes[i], nodes[j]))

#print(g)


'''Finding the shortest path'''
def printPath(path):
    '''Assumes path is a list of nodes'''
    result = ''
    for i in range(len(path)):
        result = result + str(path[i])
        if i != len(path) - 1:
            result = result + '->'
    return result

def DFS(graph, start, end, path, shortest, toPrint = False):
    '''Assumes graph is a Digraph; start and end are nodes;
          path and shortest are lists of nodes
       returns a shortest path from start to end in graph'''
    path = path + [start]
    if toPrint:
        print('Current DFS path:', printPath(path))
    if start == end:
        return path
    for node in graph.childrenOf(start):
        if node not in path: #avoid cycles
            if shortest == None or len(path) < len(shortest):
                newPath = DFS(graph, node, end, path, shortest, toPrint)
                if newPath != None:
                    shortest = newPath
        elif toPrint:
            print('Already visited', node)
    return shortest

def shortestPath(graph, start, end, toPrint = False):
    '''Assumes graph is a Digraph; start and end are nodes
       Returns a shortest path from start to end in graph'''
    return DFS(graph, start, end, [], None, toPrint)

def testSP(source, destination):
    g = buildCityGraph(Digraph)
    sp = shortestPath(g, g.getNode(source), g.getNode(destination),
                      toPrint = True)
    if sp != None:
        print('Shortest path from', source, 'to',
              destination, 'is', printPath(sp))
    else:
        print('There is no path from', source, 'to', destination)

testSP('Chicago', 'Boston')
print('-------')
testSP('Boston', 'Phoenix')

