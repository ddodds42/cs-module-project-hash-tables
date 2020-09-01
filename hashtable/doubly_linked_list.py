"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
# import sys
# sys.path.insert(1, "../stack/")
from linked_list import Node, LinkedList

class ListNode(Node):
    def __init__(self, key, value): # , next_node, next=None
        super().__init__(value)
        self.key = key
        self.prev = None
        # self.next = None
    def get_prev(self):
        return self.prev
    def set_prev(self, new_prev):
        self.prev = new_prev

# class ListNode:
#     def __init__(self, value, prev=None, next=None):
#         self.prev = prev
#         self.value = value
#         self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, key, value):
        new_node = ListNode(key, value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            prev_head = self.head
            prev_head.set_prev(new_node)
            self.head = new_node
            self.head.set_next(prev_head)
            self.length += 1
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if not self.head:
            return None
        if not self.head.get_next():
            prev_head = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return prev_head.get_value()
        value = self.head.get_value()
        self.head = self.head.get_next()
        self.head.prev = None
        self.length -= 1
        return value
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, key, value):
        new_node = ListNode(key, value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            # congruent with else statement in add_to_head. \
            # Correct w/o instantiating prev_tail?
            new_node.set_prev(self.tail)
            self.tail.set_next(new_node)
            self.tail = new_node
            self.length +=1

            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if not self.head:
            return None
        if not self.head.get_next():
            prev_head = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return prev_head.get_value()
        value = self.tail.get_value()
        self.tail = previoso
        self.tail.next = None
        self.length -= 1
        # return value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if not self.head.get_next():
            pass
        if node is self.head:
            pass
        if node is self.tail:
            self.add_to_head(node)
            self.remove_from_tail()
        else:
            infront = node.get_prev()
            behind = node.get_next()
            infront.set_next(behind)
            behind.set_prev(infront)
            self.length -= 1
            self.add_to_head(node)
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if not self.head.get_next():
            pass
        if node is self.tail:
            pass
        if node is self.head:
            self.add_to_tail(node)
            self.remove_from_head()
        else:
            infront = node.get_prev()
            behind = node.get_next()
            infront.set_next(behind)
            behind.set_prev(infront)
            self.length -= 1
            self.add_to_tail(node)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if not self.head.get_next():
            pass
        if node is self.tail:
            return self.remove_from_tail()
        if node is self.head:
            return self.remove_from_head()
        else:
            infront = node.get_prev()
            behind = node.get_next()
            infront.set_next(behind)
            behind.set_prev(infront)
            self.length -= 1

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        if not self.head:
            return None
        max_value = self.head.get_value()
        current = self.head.get_next()
        while current:
            if current.get_value() > max_value:
                max_value = current.get_value()
            current = current.get_next()
        return max_value
    
    def print_links(self):
        current = self.head
        while current:
            print(current.value)
            current = current.get_next()

lynx = DoublyLinkedList()
lynx.add_to_tail('Super', 'Julie')
lynx.add_to_tail('kala', 'Andrews')
lynx.add_to_tail('fragile', 'mary')
lynx.add_to_tail('istic', 'poppins')
# lynx.add_to_tail('expi')
# lynx.add_to_tail('ali')
# lynx.add_to_tail('docious')
lynx.print_links()
print('\n')

lynx.remove_from_tail()
print('\n')
lynx.print_links()
# print(lynx.tail.value)