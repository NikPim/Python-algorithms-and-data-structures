
import hashlib
class HashTable:
    def __init__(self, size):
        self.size = size
        self.hash_table = [[] for _ in range(self.size)]
    
    def __str__(self):
        return "".join(str(item) for item in self.hash_table)

    def set(self, key, val):
        hashed_key = hash(key) % self.size
        bucket = self.hash_table[hashed_key]
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record
            if record_key == key:
                found_key = True
        if found_key:
            bucket[index] = (key, val)
        else:
            bucket.append((key, val))

    def get(self, key):
        hashed_key = hash(key) % self.size
        print('get')
        bucket = self.hash_table[hashed_key]
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record
            if record_key == key:
                found_key = True
        if found_key:
            return record_val
        else:
            return "No record found"

    def delete(self,key):
        hashed_key = hash(key) % self.size
        bucket = self.hash_table[hashed_key]
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record
            if record_key == key:
                found_key = True
        if found_key:
            bucket.pop(index)
        else:
            return
        
    def keys(self):
        keys = []
        for i in self.hash_table:
            if i and len(i)>1:
                for j in i:
                    keys.append(j[0])
            elif i:
                keys.append(i[0][0])
        return keys



hasht = HashTable(3)
# print(hasht)
hasht.set('name', 'Nikita')
hasht.set('namesg', 'Gadf')
# print(hasht)
hasht.set('names', 'Egor')
# print(hasht)
# print(hasht.get('name'))
print(hasht)
print('keys')
print(hasht.keys())