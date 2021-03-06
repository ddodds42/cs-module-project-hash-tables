class Node:
    """
    Data:
    Stores two pieces of data:
    1. The Value
    2. The Next Node

    Methods/Behavior/Operations:
    1. Get value
    2. Set value
    3. Get next
    4. Set next
    """
    def __init__(self, key=None, value=None, next_node=None):
        self.key = key
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next = next_node
    
    # def get_key(self):
    #     return self.key

    # def get_value(self):
    #     return self.value

    # def get_next(self):
    #     return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next = new_next


class LinkedList:
    """
    Data:
    1. A reference to the head Node
    2. A reference to the tail Node

    Behavior/Methods:
    1. Add To Tail
    2. Prepend (Add a new node and point that Node's next_node at the old Head; update Head pointer)
    3. Remove Head
    4. Remove Tail
    5. Contains?
    6. Get Maximum?
    """
    def __init__(self):
        # reference to the head of the list
        self.head = None
        # reference to the tail of the list
        self.tail = None
        self.length = 0

    def add_to_tail(self, key, value):
        # wrap the input value in a node
        new_node = Node(key, value)
        # check if there is no head (i.e., the list is empty)
        if not self.head:
            # if the list is initially empty, set both head and tail to the new node
            self.head = new_node
            self.tail = new_node
            self.length += 1
        # we have a non-empty list, add the new node to the tail
        else:
            # set the current tail's next reference to our new node
            self.tail.set_next(new_node)
            # set the list's tail reference to the new node
            self.tail = new_node
            self.length += 1

    def remove_head(self):
        # return None if there is no head (i.e. the list is empty)
        if not self.head:
            return None
        # if head has no next, then we have a single element in our list
        if not self.head.next:
            # get a reference to the head
            head = self.head
            # delete the list's head reference
            self.head = None
            # also make sure the tail reference doesn't refer to anything
            self.tail = None
            self.length -= 1
            # return the value
            return head.value
        # otherwise we have more than one element in our list
        value = self.head.value
        # set the head reference to the current head's next node in the list
        self.head = self.head.next
        self.length -= 1
        return value

    def remove_tail(self):
        if not self.head:
            return None
        
        if self.head is self.tail:
            value = self.head.value
            self.head = None
            self.tail = None
            self.length -= 1
            return value
        
        current = self.head

        while current.next is not self.tail:
            current = current.next
        
        value = self.tail.value
        self.tail = current
        self.tail.next = None
        self.length -= 1
        return value

    def contains(self, value):
        if not self.head:
            return False

        # Recursive solution
        # def search(node):
        #   if node.value == value:
        #     return True
        #   if not node.next:
        #     return False
        #   return search(node.next)
        # return search(self.head)
    
        # get a reference to the node we're currently at; update this as we traverse the list
        current = self.head
        # check to see if we're at a valid node 
        while current:
            # return True if the current value we're looking at matches our target value
            if current.value == value:
                return current
            # update our current node to the current node's next node
            current = current.next
        # if we've gotten here, then the target node isn't in our list
        return f'{value} value not found.'
    
    def find(self, key):
        cur = self.head
        prev = None
        while cur:
            if cur.key == key:
                return {'cur':cur, 'prev': prev}
            prev = cur
            cur = cur.next
        return f"Key '{key}' not found"


    def get_max(self):
        if not self.head:
            return None
        # reference to the largest value we've seen so far
        max_value = self.head.value
        # reference to our current node as we traverse the list
        current = self.head.next
        # check to see if we're still at a valid list node
        while current:
            # check to see if the current value is greater than the max_value
            if current.value > max_value:
                # if so, update our max_value variable
                max_value = current.value
            # update the current node to the next node in the list
            current = current.next
        return max_value
    
    def print_links(self):
        current = self.head
        while current:
            print(current.key, ':', current.value)
            current = current.next

if __name__ == "__main__":
    lank = LinkedList()
    lank.add_to_tail('Super', 'Julie')
    lank.add_to_tail('kala', 'Andrews')
    lank.add_to_tail('fragile', 'mary')
    lank.add_to_tail('istic', 'poppins')
    lank.add_to_tail('expi', 'Sound')
    lank.add_to_tail('ali', 'of')
    lank.add_to_tail('docious', 'Music')
    lank.print_links()
    print('\n')
    print(lank.find('docious'))
    print('\n')
    print(lank.find('docious')['prev'])