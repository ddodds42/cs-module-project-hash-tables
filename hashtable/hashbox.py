from hashtable import HashTable

capacity = 20

# def djb2(key):
#     hash = 5831
#     for c in key:
#         hash = (hash*33) + ord(c)
#     return hash

# def hash_index(key):
#     return djb2(key) % capacity

# def put(self, key, value):
#     indx = self.hash_index(key)
#     self.storage_array[indx] = value

tably = HashTable(capacity)

tably.put('I', 'you')
tably.put('am', 'be')
tably.put('the', 'a')
tably.put('mountain', 'hill')

print(tably.delete('I'))
print(tably.delete('am'))
print(tably.delete('the'))
print(tably.delete('mountain'))

print(tably.storage_array)