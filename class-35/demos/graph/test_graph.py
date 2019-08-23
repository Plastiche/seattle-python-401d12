import pytest
from graph import Graph, Vertex

"""
X Node can be successfully added to the graph
X An edge can be successfully added to the graph
X A collection of all nodes can be properly retrieved from the graph
X All appropriate neighbors can be retrieved from the graph
X Neighbors are returned with the weight between nodes included
X The proper size is returned, representing the number of nodes in the graph
X A graph with only one node and edge can be properly returned
X An empty graph properly returns null
"""

def test_exists():
    assert Graph
    assert Vertex

def test_add_single():
    g = Graph()
    apples = g.add_vertex('apples')
    assert isinstance(apples, Vertex)
    assert apples.value == 'apples'

def test_add_multiple():
    g = Graph()
    apples = g.add_vertex('apples')
    bananas = g.add_vertex('bananas')
    cucumbers = g.add_vertex('cucumbers')
    assert apples.value == 'apples'
    assert bananas.value == 'bananas'
    assert cucumbers.value == 'cucumbers'

def test_get_single():
    g = Graph()
    apples = g.add_vertex('apples')
    nodes = g.get_vertices()
    assert len(nodes) == 1
    assert nodes[0].value == 'apples'

def test_get_multiple():
    g = Graph()
    g.add_vertex('apples')
    g.add_vertex('bananas')
    g.add_vertex('cucumbers')
    nodes = g.get_vertices()
    assert len(nodes) == 3
    assert { node.value for node in nodes } == set(['apples','bananas','cucumbers'])

def test_length():
    g = Graph()
    g.add_vertex('apples')
    g.add_vertex('bananas')
    assert len(g) == 2

def test_empty():

    g = Graph()

    assert g.get_vertices() == None

def test_add_edge():
    g = Graph()
    apples = g.add_vertex('apples')
    bananas = g.add_vertex('bananas')
    g.add_edge(apples, bananas, 15)
    
    apples_bananas_edge = apples.neighbors[0]

    assert apples_bananas_edge.vertex == bananas

    assert apples_bananas_edge.weight == 15

    assert len(bananas.neighbors) == 0

def test_get_neighbors():
    g = Graph()
    apples = g.add_vertex('apples')
    bananas = g.add_vertex('bananas')
    cucumbers = g.add_vertex('cucumbers')
    g.add_edge(apples, bananas, 15)
    g.add_edge(apples, cucumbers, 12)

    neighbors = g.get_neighbors(apples)

    assert neighbors[0].vertex.value == 'bananas'
    assert neighbors[0].weight == 15

    assert neighbors[1].vertex.value == 'cucumbers'
    assert neighbors[1].weight == 12

def test_self_loop():
    g = Graph()
    apples = g.add_vertex('apples')
    g.add_edge(apples, apples)

    neighbors = g.get_neighbors(apples)

    assert neighbors[0].vertex.value == 'apples'
    assert neighbors[0].weight == 0
    
    nodes = g.get_vertices()

    assert [node.value for node in nodes] == ['apples']


def test_breadth_first():
    g = Graph()
    apples = g.add_vertex('apples')
    bananas = g.add_vertex('bananas')
    cucumbers = g.add_vertex('cucumbers')
    g.add_edge(apples, bananas, 15)
    g.add_edge(apples, cucumbers, 12)


    visited = []
    def visit(vertex):
        visited.append(vertex.value)

    g.breadth_first(apples, visit) 
    
    assert visited == ['apples','bananas','cucumbers']



