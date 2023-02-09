# Chapter 1

Things to Know/Review
- linked lists, BSTs, and Priority Queues
- Discrete Math: 
	- definitions, properties, notations of tuples, sets, multisets, and sequences
	- set theory
	- cartesian product, subsets, and permutations
	- probability, dependence, expected value
	- mapping, injection, surjection, associative, commutative, distributive, trasitive
	- conjunction, disjunction, equivalence, implication, negation, and DeMorgan's law
	- proofs, direct argument, contradiction, induction, constructive proofs, the pigeonhole principle
	- vertices, edges, labels, directedness, paths, cycles, and connectivity

# Chapter 2

**Data**: a finite mathematical object that can be represented by a binary string

**Problem**: An input/output specification which specifies the data type as well as any constraints
Ex:
##### Mininum Problem
**Input**: A non-empty list **L** of **n** orderable objects
**Output**: The least (minimum) element in **L**

A problem instance is a valid input object for a specific problem and a solution is the corresponding output.

**Algorithm**: A defined series of steps/actions directed to some end which, given an instance of a problem, produces a solution for that instance and has the properties of clarity, correctness, and termination. Clarity means that the algorithm is described clearly enough to be implemented, correctness that it always produces the same solution, and termination that it takes a finite amount of time.

**Pseudocode Checklist**
1. inputs and outputs clearly defined and separate from all variables
2. no variables are undefined
3. variable meanings are clear and confusing names are explained
4. all fucntions have a return value
5. return value matches data type of specification
6. handle all cases, such as empty inputs, etc...
7. no infinte loops
8. every recursive function has a base case
9. any repetitive code is grouped into a helper function
10. no nonexecuting code
11. eliminate vagueness fom code

An **algorithm pattern** is a problem agnostic approach to designing algorithms. It is a template that can be used as a starting point with the specific details coming from the given problem.

Steps to design and analyze an algorithm:
1. Clearly define the problem
2. Choose an appropriate pattern
3. Write a first draft using the pattern skeleton
4. Revise your draft by filling in blanks, repeat until pseudocode is correct, terminates, and is clear.
5. Edit draft for cleaness and clarity
6. Prove the correctness of the algorithm
7. Prove the efficiency of the algorithm

