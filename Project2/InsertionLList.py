# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 11:20:45 2024

@author: Shawn Fahy
"""

# Node class  
class Node:  
      
    # Constructor to initialize the node object  
    def __init__(self, data):  
        self.data = data  
        self.next = None

# function to sort linked list using insertion sort 
def insertionSort(head): 
  
    # Initialize sorted linked list 
    sorted = None
  
    # Traverse the given linked list and insert every node to sorted
    current = head
    while (current != None): 
      
        # Store next for next iteration 
        next = current.next
  
        # insert current in sorted linked list 
        sorted = sortedInsert(sorted, current) 
  
        # Update current 
        current = next
      
    # Update head variable to point to sorted linked list 
    head = sorted
    return head
  
# function to insert a node in a linked list in a sorted manner
def sortedInsert(head, new_node): 
  
    current = None
      
    # Special case for the head end */ 
    if (head == None or (head).data >= new_node.data): 
        new_node.next = head
        head = new_node 
      
    else: 
      
        # Locate the node before the point of insertion  
        current = head
        while (current.next != None and
            current.next.data < new_node.data): 
            current = current.next
          
        new_node.next = current.next
        current.next = new_node 
          
    return head
  
  
# Function to print linked list
def printList(head): 
  
    temp = head 
    while(temp != None): 
      
        print( temp.data, end = " ") 
        temp = temp.next
      
# function to insert node at beginning of a linked list
def insertAtStart(head_ref, new_data): 
  
    # allocate node 
    new_node = Node(0) 
  
    # put in the data  
    new_node.data = new_data 
  
    # link the old list of the new node  
    new_node.next = (head_ref) 
  
    # move the head to point to the new node  
    (head_ref) = new_node 
    return head_ref

a = None
# open and strip
with open('random5k.txt') as file:
    for fline in file:
        a = insertAtStart(a, (int(fline.strip())))
printList(a)
a = insertionSort(a)
printList(a)

