

# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# '''
# Fill this in

# Resizing hash table
# '''
class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None]*capacity
        


# '''
# Research and implement the djb2 hash function
# '''
def hash(string, max):
    hash = 5381
    for x in string:
        hash = (( hash << 5) + hash) + ord(x)
    return hash & 0xFFFFFFFF % max


# '''
# Fill this in.
def _link_traversal(link_item,key,value):
   

    if link_item.next is None:
        link_item.next = LinkedPair(key,value)
        print(f"inserted {value} as LinkedPair")
        return

    elif link_item.next.key == key:
        link_item.next.value = value
        print(f"OVERWROTE LINKED with {value} at key {key}")
        return

    else:
        _link_traversal(link_item.next)

def _link_traversal_return(link_item,key):
   

    if link_item == None:
        print("None  condition firing")
        
        return "No item found"

    elif link_item.key == key:
        print("Match condition firing")
        print(f"Found LINKED with {link_item.value} at key {key}")
        return link_item.value

    else:
        print("return else condition firing")
        _link_traversal_return(link_item.next)
    

# Hint: Used the LL to handle collisions
# '''
def hash_table_insert(hash_table, key, value):
    hashed_key = hash(key,hash_table.capacity)
    

    if hash_table.storage[hashed_key] !=  None:
        
        if hash_table.storage[hashed_key].key == key:
            hash_table.storage[hashed_key].value = value
            print(f"OVERWROTE with {value} at key {key}")
       


        else:
            
            _link_traversal(hash_table.storage[hashed_key],key,value)
            


    else:
        hash_table.storage[hashed_key] = LinkedPair(key,value)
        print(f"inserted BCNONE {value} at {hashed_key}")


# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    hashed_key = hash(key,hash_table.capacity)
    if hash_table.storage[hashed_key] is None:
        print(f"No value at{hashed_key}")
    else:
        #this doesn't account for different values with the same key, will replace entire
        #linked lists with none
         hash_table.storage[hashed_key] = None
# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    hashed_key = hash(key,hash_table.capacity)
    if hash_table.storage[hashed_key] is None:
        print(f"No value found at {hashed_key}")

    elif hash_table.storage[hashed_key].key == key:
        #if the key matches the first return value
            return hash_table.storage[hashed_key].value

  
    elif hash_table.storage[hashed_key].key != key:
        print(f"collision at {hashed_key} and {key}")
        return _link_traversal_return(hash_table.storage[hashed_key].next,key)
          #if there is a collision chain, iterate through next item until retrieval key matches
       
        
        
       
        


# '''
# Fill this in
# '''

def hash_table_resize(hash_table):
    #calc load factor
    #assess current load factor
    #if appropriate creat new doubled hashtable
    #loop over storage of old table
    #assess of multiple values are stored under same hash in old
    #if so creat sub loop to reassign those values
    #else assign values as you ordinarily would
  


    load_factor = (hash_table.capacity - hash_table.storage.count(None))/hash_table.capacity
    if load_factor >= .7:
        new_storage = HashTable(hash_table.capacity*2)
        old_storage = hash_table.storage
        for i in range(len(old_storage)):
            #at first level of array copy over to new_storage
            hash_table_insert(new_storage, old_storage[i].key, old_storage[i].value)
       

            #check for linked hashes resulting from collisions
            #give new hash key based on resized array

            next_linked_hash = old_storage[i].next
            while next_linked_hash is not None:
                nested_hash = next_linked_hash.key
                nested_value = next_linked_hash.value
                hash_table_insert(new_storage, nested_hash, nested_value)
                next_linked_hash = next_linked_hash.next

        
        return new_storage
            

                



def Testing():
    ht = HashTable(2)

    hash_table_insert(ht, "line_1", "Tiny hash table")
    hash_table_insert(ht, "line_2", "Filled beyond capacity")
    hash_table_insert(ht, "line_3", "Linked list saves the day!")

    print(hash_table_retrieve(ht, "line_1"))
    print(hash_table_retrieve(ht, "line_2"))
    print(hash_table_retrieve(ht, "line_3"))

    old_capacity = len(ht.storage)
    ht = hash_table_resize(ht)
    new_capacity = len(ht.storage)

    print("Resized hash table from " + str(old_capacity)
          + " to " + str(new_capacity) + ".")


Testing()
