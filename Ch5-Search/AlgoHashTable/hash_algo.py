class AlgoHashTable:

    def __init__(self, size):
        self.size = size
        self.hash_table = self.create_buckets()

    def create_buckets(self):
        return [[] for _ in range(self.size)]

    def set_val(self, key, value):
        # hash the email passed in as key and mod it by size, because the raw hash could be too big
        hashed_key = hash(key)%self.size
        bucket = self.hash_table[hashed_key]

        found_key = False
        for index, record in enumerate(bucket):
            # unpack record
            record_key, record_value = record
            if record_key == key:
                found_key = True
                break

            if found_key:
                # if key exists, update the value
                bucket[index] = (key, value)
            else:
                # insert new value
                bucket.append((key, value))

    def get_val(self, key):
        # hash the email passed in as key and mod it by size, because the raw hash could be too big
        hashed_key = hash(key)%self.size
        bucket = self.hash_table[hashed_key]

        found_key = False
        for index, record in enumerate(bucket):
            # unpack record
            record_key, record_value = record
            if record_key == key:
                found_key = True
                break
        if found_key:
            return record_value
        else:
            return "No record found with that email address"


    def del_val(self, key):
        pass

    def __str__(self):
        return "".join(str(item) for item in self.hash_table)


hash_table = AlgoHashTable(256)
print(hash_table)

hash_table.set_val('tommac@example.com', 'some value')
hash_table.set_val('kobe@example.com', 'Mamba')
# hash_table.set_val('tommac@example.com', 'FB Job')

print(hash_table)

hash_table.get_val('tommac@example.com')