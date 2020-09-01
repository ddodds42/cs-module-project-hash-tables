from hashtable import HashTable
from doubly_linked_list import DoublyLinkedList

capacity = 20

tably = HashTable(capacity)

tably.storage_array[0].add_to_tail('I', 0)
tably.storage_array[0].add_to_tail('am', 1)
tably.storage_array[0].add_to_tail('the', 2)
tably.storage_array[0].add_to_tail('mountain', 3)

tably.storage_array[1].add_to_tail('you', 4)
tably.storage_array[1].add_to_tail('be', 5)
tably.storage_array[1].add_to_tail('a', 6)
tably.storage_array[1].add_to_tail('hill', 7)

tably.storage_array[0].print_links()
print('\n')
tably.storage_array[1].print_links()

'''
tably.put('I', 'you')
tably.put('am', 'be')
tably.put('the', 'a')
tably.put('mountain', 'hill')
tably.put('sea', 'ocean')

print('mountain index = ', tably.hash_index('mountain'))
print('sky index = ', tably.hash_index('sky'), '\n')

print('mountain before potential collision: ', tably.get('mountain'), '\n')

tably.put('sky', 'wind')

print('mountain, collision averted: ', tably.get('mountain'))
print('sky, collision averted: ', tably.get('sky'), '\n')

print(
    'the linked list itself: '
)
tably.storage_array[14].print_links()
print('\n')

print(tably.deleter('sky'), '\n')

print('mountain still there: ', tably.get('mountain'))
print('sky still there: ', tably.get('sky'), '\n')
'''