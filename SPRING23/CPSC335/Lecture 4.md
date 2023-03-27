**Spanning Trees**: a subgraph T = (V,K) of a graph G = (V, E) where K is a  subset of E.
All spanning trees of a graph have yhe same number of edges and vertices. No cycles. Even removing one edge will cause it to cease being a spanning tree as it is minimally connected.

A graph that uses the least number of edges to connet the vertices is a spanning tree. 
The minimum spanning tree is the spanning tree of a weighted graph with the minimal weight. May not be unique if the edge weights are not unique. 

Minimum Spanning Tree Problem
**Input**: connected, undirected, weighted graph G =(V, E) with n = |V| and m = |E|
**Output**: A set of edges K st T - (V,K) is a minimum spanning tree for G
```python
def greedy_mst(G):
	K = set()
	while K.edges() != G.edges():
		e = choose_edge(G)
		K.add(e)
	return K
```

MST has applications in designing LANs, Civil Network Planning, computer network routing, laying pipelines, and cluster analysis.

**Bridge Edges**: For a graph that is partitioned into two sides L and R st L U R = V, any edge that connects L and R is called a bridge edge. A least weight edge is the best choice to connect an MST. 
**Bridge Theorem**: The bridge edge of least weight between partitions inside the graph  will be included in the MST

```python
def greedy_mst(G):
	K = set()
	p = partition(G)
	while len(K) < G.vertex_count() -1:
		e = minimum_weight_bridge(p)
		K.add(e)
		partition(G)
	return K
```

**Prim's algorithm**: is a greedy technique for finding MSTs for a give graph.

1. Start at any node, marking them as either `reached` or `unreached`.
2. Find edge `e` that connects a reach and unreached node
3. Add edge `e` found to the MST
4. Repeat 1-3 until K has the same number of vertices as G

*  `O(V^2)` however using priority queue `O(V + E * log(E))`

**Kruskal's Algorithm**:
1. Sort all the edges in non-decreasing order (weight)
2. Pick smalles edge, if it forms a cycle with the spanning tree formed so far ignore it, otherwise add it.
3. Repeat until V-1 edges

**Single Source Shortest Path**
* shortest path problems computing minimal weight paths between vertices in graphs
* single source version require us to compute such paths from a single source

