class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def hash_function(self, key, size):
        return key % size

    def rehash(self, old_hash_value, size):
        return (old_hash_value + 1) % size

    def put(self, key, data):
        hash_value = self.hash_function(key, len(self.slots))

        if self.slots[hash_value]:
            self.slots[hash_value] = key
            self.data[hash_value] = key
        elif self.slots[hash_value] == key:
            self.data[hash_value] = data
        else:
            new_hash_value = self.rehash(hash_value, len(self.slots))

            while self.slots[new_hash_value] is not None and \
                  self.slots[new_hash_value] is not key:
                new_hash_value = self.rehash(new_hash_value, len(self.slots))

            if self.slots[new_hash_value] is key:
                self.data[new_hash_value] = data
            elif self.slots[new_hash_value] is None:
                self.data[new_hash_value] = data
                self.slots[new_hash_value] = key

    def get(self, key):
        start_slot = self.hash_function(key, len(self.slots))

        data = None
        found = False
        stop = False
        position = start_slot

        while self.slots[position] is not None and not found and not stop:
            if self.slots[position] == key:
                data = self.slots[position]
                found = True
            else:
                position = self.rehash(position, len(self.slots))
                if position == start_slot:
                    stop = True
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.put(key, value)






