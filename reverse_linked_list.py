'''
Reverse a linked list
Given pointer to the head node of a linked list, 
the task is to reverse the linked list. 
We need to reverse the list by changing links between nodes.
'''
# Python program to reverse a linked list  
# Time Complexity : O(n) 
# Space Complexity : O(1) 
# prev,curr,next有严格的移动顺序，写反了会出错
'''
Initialize three pointers prev as NULL, curr as head and next as NULL.
Iterate trough the linked list. In loop, do following.
初始时，prev = Null,  curr = head,  next = Null
把next变成current前，先储存next，后再把next变current
// Before changing next of current,
// store next node
next = curr->next
// Now change next of current
// This is where actual reversing happens
curr->next = prev

// Move prev and curr one step forward
prev = curr
curr = next
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    # Function to initialize head 
    def __init__(self): 
        self.head = None

    # Function to reverse the linked list 
    def reverseList(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next      # next移动后，再prev，再current
            current.next = prev
            prev = current           # 之前这句和下面一句写反
            current = next           # 打印不出东西
        self.head = prev

    # Function to insert a new node at the beginning 
    def push(self, new_value): 
        new_node = Node(new_value)
        new_node.next = self.head
        self.head = new_node

    # Utility function to print the linked LinkedList 
    def printList(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next


# Driver program to test above functions 
llist = LinkedList() 
llist.push(20) 
llist.push(4) 
llist.push(15) 
llist.push(85) 
  
print("Given Linked List")
llist.printList() 
llist.reverseList() 
print("Reversed Linked List")
llist.printList() 