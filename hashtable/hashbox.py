from hashtable import HashTable
# from doubly_linked_list import DoublyLinkedList

capacity = 20

tably = HashTable(capacity)

print(tably.get_load_factor(), '\n')

tably.put('mountain', 'hill')
tably.put('sky', 'wind')
tably.put('Super', 'Julie')
tably.put('kala', 'Andrews')
tably.put('fragile', 'mary')
tably.put('istic', 'poppins')
tably.put('expi', 'Sound')
tably.put('ali', 'of')
tably.put('docious', 'Music')

print(tably.get_load_factor(), '\n')

tably.resize(capacity*9)

print(tably.get_load_factor(), '\n')