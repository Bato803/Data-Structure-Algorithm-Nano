Time complexity: O(1) for both get and set. 
Space complexity: O(capacity) for holding the data. 

In this problem, I choose to use dictionary to store (key, node) pair. Because in order to get O(1) in "get" operation, ustilizing the hash function in the dictionary seems to be a very natural choice. However, the tricky part of this problem is we need to maintain the right order of the elements based on their visiting history. So whenever an element is being called(either by "get" or by "set"), its order needs to be updated. 

That's where the double edge linked list comes in. To update a node's order, we can remove its origin position from the linked list without referencing its neighbors and linked it to the head of the list. The whole operation only take O(1) complexity. Imagine if we use a normal linked list for this, we'll need to keep track of its previous neighbor to achieve the same functionality, which makes the job more complex. And if we use array, deletion and insertion will take O(n). 

Also, by using a double edge linked list, we can have a pseudo head and tail to keep track of the newest and the oldest elements. Therefore, whenever the number of elements exceeds the capacity, we could remove the tail with O(1) complexity. If we use normal linked list for this, we'll need to keep track of the last few elements of the linked list in order to maintained the right tail. And it's going to be complicated for sure.  

