from hashtable import HashTable

capacity = 20

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