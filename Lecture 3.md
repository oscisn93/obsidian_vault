Hamilton problem: Given a list of cities joined in a circle, a list of the distances between them and a list of the amount of gallons of gas that can be pumped at each location as well as the mpg of the car, find the preffered city such that it results in being able to travel the full length of circle. Greedy method.

Group schedule problem: Given a set of arrays that contain time intervals where all parties are availlable, return an array of intervals when all members are simultaneously available... 

# Elementary Data Structure

**Data Structures**: containers that are used to work with groups of data, and organize them for efficient processing

**Abstract Data Types**: logical representation of data defined by its behavior, with the implemetation details left ambigious. Hides the implementation details from the user so they can focus primarily on the behavior.

**Array**: an ordered collection of fixed size elements, indexed according to integer values. O(1) access. 

**Matrix**: can be represented using by an array containing m n-sized arrays.

**Vector**: a dynamic (resizable) array of fixed size elements. supports dynamically adding and removing elements.

**Dynamic Sets**: sets that can change- such as dictionaries. key: value pairs
	queries return information or data from the set
	modifying operation mutate the sets state

**Linked List**: Set of nodes which contain data and a pointer (or pointers in the case of doubly-linked lists) to another node.

Priority Wueue  implemented using binary heap. min heap and max heap. Binaty tree always balanced, since insertions may unbalance, it must be rebalanced after each insertion.
convert  `arr = [6,4,5,3,2,0,1]`

```python3



def node(data):
	return {
		n: data,
		left: None
		right: None
	}

def arr_to_heap(arr):
	a = arr.sort(reverse=True)
	head = node(a.pop(0))
	if len(a) == 2:
		head.left = node(a.pop(0))
		head.right = node(a.pop(0))
		return head
	else:
		head.left = arr_to_heap(a[0], a[1:])	
		head.right = arr_to_heap(a[1], a[2:])
	return head
```

**Look at maxHeapify pseudocode**
insertion and deletion both require a heapify operation to restore balance to the binary tree

**Graphs**: Collection of nodes which make up the vertices and connections which are represented as edges defined by the set G(V, E). May be directed or undierected
- degree of a vertex is the number of edges on v

**Undirected Graph**: a graph which contains undirected edges- which is to say that the edge vw is the same as wv.

**Directed Graphs(Digraphs)**: graphs which contain directed edges- that is in a DG uv is not the same as vu. Edges written u -> v.

**Weighted Graphs**: graph defined by a triplet (V,E,W) where W is a numerical valued associated with a given edge. 

**Complete Graph**: A graph where every node is connected to every other node. Total number of edges = `[n(n-1)]/2`

**Adjacency Matrix (Unweighted Graph)**: 2D representation of a graph, where the presence of the value 1 denotes the two nodes are connected and a 0 indicates that there is no connection. (Adding Node takes `O(V^2)`).






