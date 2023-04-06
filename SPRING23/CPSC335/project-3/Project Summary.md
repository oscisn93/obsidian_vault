# Soccer Opponent Avoidance

The problem involves finding a shortest path from one end of a r x c (rows and columns, respectively) grid to the diagonal opposite end where there exist several cells that must be traversed around rather than through. It is meant to represent the movement of a soccer player across the field in order to reach the opposing goal post safely and potentially score. The exception of course is that in this formulation of the problem the opponent (represented by the impenetrable cells) is at fixed locations. 
Sample input for this file looks like this:
```in
...... X . X
X ........
... X ... X .
.. X .... X .
. X .... X ..
.... X ....
.. X ..... X
.........
```

Coordintate (0,0) is at the top left  and the target coordinate is (r-1, c-1). We are to find all possible paths. Paths are different if they differ by any given cell.
The expected output for the sample input above is `102`

# Exhaustive Search
first draft:
```python
def soccer_exhaustive(G):  
	maxno = total number of different paths originating at (0,0) and ending at (𝑟 − 1, 𝑐 − 1)  
	counter = 0 (number of valid paths in G)  
	for len from 0 to maxno inclusive:  
		for each possible sequence S of {→, ↓} encoded as len:  
			candidate = [start] + S  
			if candidate is valid:  
				counter++  
	return counter
```
 
Second:

```python
def soccer_exhaustive(G):  
	len = 𝑟 + 𝑐 − 2  
	counter = 0  
	for bits from 0 to 2^𝑙𝑒𝑛 − 1 inclusive:  
		candidate = empty list of moves  
		for k from 0 𝑡𝑜 𝑙𝑒𝑛 − 1 inclusive:  
			bit = (bits >> 𝑘) & 1  
			if bit == 1:  
				candidate.add(→)  
			else:  
				candidate.add(↓)  
		if candidate stays inside the grid, never crosses an X cell, and ends at (𝑟 − 1, 𝑐 − 1):  
			counter++  
	return counter
```


# Dynamic Programming
```python
def soccer_dyn_prog(F):
	if 𝐹[0][0] == 𝑋:  
		return 0  
	A = new 𝑟⨉𝑐 matrix initialized to zeroes  
	# base case  
	A[0][0] = 1  
	# general cases  
	for 𝑖 from 0 𝑡𝑜 𝑟 − 1 inclusive:  
		for 𝑗 𝑓𝑟𝑜𝑚 0 𝑡𝑜 𝑐 − 1 inclusive:  
			if F[𝑖][𝑗] == 𝑋:  
				𝐴[𝑖][𝑗] = 0  
				continue  
			above = 𝑓𝑟𝑜𝑚_𝑙𝑒𝑓𝑡 = 0  
			if 𝑖 > 0 𝑎𝑛𝑑 𝐹[𝑖 − 1][𝑗] == . :  
				above = 𝐴[𝑖 − 1][𝑗]  
			if 𝑗 > 0 and 𝐹[𝑖][𝑗 − 1] == . :  
				left = 𝐴[𝑖][𝑗 − 1]  
			𝐴[𝑖][𝑗] += 𝑎𝑏𝑜𝑣𝑒 + 𝑙𝑒𝑓𝑡  
	return 𝐴[𝑟 − 1][𝑐 − 1]
```

# Hypotheses

1. Exhaustive search algorithms can be implemented, and produce correct outputs.
2. Algorithms with exponential or factorial running times are extremely slow, probably too slow to be of practical use.

# Report

Include title, scatter plots for both algorithms, and name and email.
Answer questions:
1. Is there a noticeable difference in the performance of the two algorithms?
2. According to experimental observation, which of the implementations is faster and by how much?
3. Are empirical analyses consistent with the predicted big-O efficiency class for each algorithm? Justify.
4. Is this evidence consistent with Hypothesis 1? Justify.
5. Is this evidence consistent with Hypothesis 2? Justify.

