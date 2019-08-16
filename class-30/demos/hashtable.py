from linked_list import LinkedList

class HashTable:
    
    def __init__(self):
        self.buckets = [LinkedList()] * 1024


    def hash(self, key):

        char_sum = sum([ord(char) for char in key])

        prime_number = 599
        
        index = char_sum * prime_number % len(self.buckets)

        return index

    def add(self, key, value):

        index = self.hash(key)

        bucket = self.buckets[index]

        bucket.insert({'key':key, 'value':value})


    def get(self, key):

        index = self.hash(key)

        bucket = self.buckets[index]

        # traverse through bucket (aka linked list)
        # to find matching key and return corresponding value

        return None # or raise Exception if you like




