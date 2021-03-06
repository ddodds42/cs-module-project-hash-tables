# from doubly_linked_list import DoublyLinkedList
from linked_list import LinkedList

class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8
# lank = DoublyLinkedList()


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys
    """
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage_array = [LinkedList() for i in range(capacity)]

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.
        """
        return self.capacity

    def num_records(self):
        # counter
        slots = 0
        for linklist in self.storage_array:
            # increment counter with each list's length
            slots += linklist.length
        return slots

    def get_load_factor(self):
        return self.num_records()/self.capacity


    def fnv1(self, key):
        # FNV-1 Hash, 64-bit
        # Implement this, and/or DJB2.
        pass


    def djb2(self, key):
        # DJB2 hash, 32-bit
        hash = 5831
        for c in key:
            hash = (hash*33) + ord(c)
        return hash


    def hash_index(self, key):
        # Take an arbitrary key and return a valid integer index
        # between within the storage capacity of the hash table.

        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        # Store the value with the given key.
        # Hash collisions should be handled with Linked List Chaining.
        if self.get_load_factor() >= 0.7:
            self.resize(self.capacity*2)

        indx = self.hash_index(key)
        nodes = self.storage_array[indx].find(key)
        if type(nodes) is dict:
            nodes['cur'].key = key
            nodes['cur'].value = value
            self.storage_array[indx].length +=1
            return
        self.storage_array[indx].add_to_tail(key, value)

    def delete(self, key):
        # Remove the value stored with the given key.
        # Print a warning if the key is not found.
        indx = self.hash_index(key)
        lank = self.storage_array[indx]
        nodes = lank.find(key)

        if type(nodes) is dict:
            if nodes['prev']:
                nodes['prev'].next = nodes['cur'].next
                lank.length -= 1
            elif not nodes['prev']:
                lank.remove_head()
            else:
                lank.remove_tail()
            return nodes['cur'].key, nodes['cur'].value
        return nodes

    def get(self, key):
        # Retrieve the value stored with the given key.
        # Returns None if the key is not found.
        indx = self.hash_index(key)
        lank = self.storage_array[indx]
        nodes = lank.find(key)

        if type(nodes) is dict:
            return nodes['cur'].value
        return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.
        """
        new_ht = HashTable(new_capacity)
        for linklist in self.storage_array:
            cur = linklist.head
            while cur:
                new_ht.put(cur.key, cur.value)
                cur = cur.next
        self.capacity = new_capacity
        self.storage_array = new_ht.storage_array


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print()

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print()
