To implement huffman coding, there are several key factors we need to consider: 

1) Easy access to the characters with minimum frequency. Accessing least frequent characters operation is repeated lots of times when we are building the huffman tree. It's very important to ensure we can have O(1) time complexity to access min frequent character. Otherwise say if we have O(logN) or O(N) in accessing min frequency character, then the recursive/iterative operation in building the huffman tree is going to take at least O(NlogN) or O(N^2) (Assume it takes O(n) to build the tree). But if we have O(1) in accessing min frequent character, we can ensure we are not adding any multiplicative factor to the time complexity. 

Key take-away: Use min Heap to ensure easy access to min frequent character. 


2) What to save in the heap. We know that heap is normally implemented using array, but in our case we have plenty of information to store in each entry of this array. For example, we'll need to store the character, its frequency, and its relations with other characters in the huffman tree. And it would also be better if this data structure support comparison operation between each other, because we need them in using heap pop or heap push operation. 

Key take-away: Implement a customized data structure Node, who has value and frequency as its attribute, as well left/right to connect to other Node in the heap. Comparison operations such as "less than" and "more than" should also be included in this data structure. 


3) Complexity Analysis: 

Assume N is the length of the input text: 

- Construct frequency table: O(n)
- Construct huffman tree: O(NlogN)
    - Finding Min: O(1) 
	- Heap pop: O(logN)
	- Merge Node: O(1)
	- Heap push: O(logN)
	- Iterating the Heap: O(N)
- Getting encoded text: O(N)
	- Iterate through text: O(N)
	- Accessing corresponding code: O(1)
- Decoding: similar to encoding O(N)

- Memory complexity: O(N)
	- Saving frequency table: O(N)
	- Saving text-code relation: O(N)

Overall time and memory complexity: O(NlogN) and O(N)