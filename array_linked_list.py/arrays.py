

# Do not use any of the built in array functions for this exercise
class array:
    def __init__(self,capacity):
        self.capacity = capacity
        self.elements = [None]*capacity
       


# Double the size of the given array
    def resize_array(self):
        # Your code here
        new_array = (self.capacity*2)*[None]#is this always O(n)?
        print("New len",new_array)
        for i in range(len(self.elements)):
            new_array[i] = self.elements[i]

        self.elements = new_array
        self.capacity = len(new_array)



# Return an element of a given array at a given index
    def array_read(self, index):
        if index > self.capacity -1:
            print("Supplied index not in range of array")
        
        else:
            return self.elements[index]
        
        # Throw an error if array is out of the current count
        # Your code here
        


# Insert an element in a given array at a given index
    def array_insert(self,element,index):
        # Throw an error if array is out of the current count
        # if index > self.capacity -1:
        #     print("Supplied index not in range of array")
        #https://stackoverflow.com/questions/33044883/why-is-the-time-complexity-of-pythons-list-append-method-o1
        #https://en.wikipedia.org/wiki/Amortized_analysis
        #  each time you resize, you take about twice as much time as the last resize. But you've also waited twice as long before doing it! The cost of each resize can thus be "spread out" among the insertions. This means that in the long term, the total time taken for adding m items to the array is O(m), and so the amortised time (i.e. time per insertion) is O(1).

        if (self.capacity - self.elements.count(None)) == self.capacity:
            self.resize_array()
            print("None count",self.elements.count(None))
            print(self.elements)
            print(self.capacity)
            for i in range(self.capacity-1,index,-1):
                print(i)
                self.elements[i] = self.elements[i -1]
            
            self.elements[index] = element
            
        
        else:
            for i in range(self.capacity-1,index,-1):
                
                self.elements[i] = self.elements[i -1]
            self.elements[index] = element
            
          
                

        # Resize the array if the number of elements is over capacity

        # Move the elements to create a space at 'index'
        # Think about where to start!

        # Add the new element to the array and update the count
    


    # Add an element to the end of the given array
    def array_append():

        # Hint, this can be done with one line of code
        # (Without using a built in function)

        # Your code here
        pass


    # Remove the first occurence of the given element from the array
    # Throw an error if the value is not found
    def array_remove():
        # Your code here
        pass


    # Remove the element in a given position and return it
    # Then shift every element after that occurrance to fill the gap
    def array_pop():
        # Throw an error if array is out of the current count
        # Your code here
        pass


# Utility to print an array
    def array_print(self):
        string = "["
        for i in range(len(self.elements)):
            string += str(arr.elements[i])
            if i < len(self.elements) - 1:
                string += ", "

        string += "]"
        print(string)


# # Testing
arr = array(1)
print(arr.elements)

arr.array_insert("STRING1", 0)
arr.array_print()

# array_print(arr)
# array_pop(arr, 0)
# array_print(arr)
# array_insert(arr, "STRING1", 0)
# array_append(arr, "STRING4")
arr.array_insert("STRING2", 1)
arr.array_insert("STRING3", 2)
arr.array_print()
arr.array_insert("STRINGX", 1)
arr.array_insert("STRINGY", 1)
arr.array_print()
# print(arr.capacity)
print(arr.elements)
