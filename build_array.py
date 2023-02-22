import ctypes
 
class OurOwnList(object):
     
    def __init__(self):
        # Count actual elements (Default is 0)
        self.n = 0
 
        # Default Capacity
        self.capacity = 1
        self.A = self.make_array(self.capacity)
        

    def __len__(self):
        """
        Return number of elements sorted in array
        """
        return self.n
     
    def __getitem__(self,k):
        """
        Return element at index k
        """
        if not 0 <= k <self.n:
            # Check it k index is in bounds of array
            return IndexError('K is out of bounds!') 
 
        #Retrieve from array at index k
        return self.A[k] 
         
    def append(self, ele):
        """
        Add element to end of the array
        """
 
        if self.n == self.capacity:
            self._resize(2*self.capacity) #Double capacity once overflow
         
        self.A[self.n] = ele #Set self.n index to element
        self.n += 1
         
    def _resize(self,new_cap):
        """
        Resize internal array to capacity new_cap
        """
         
        B = self.make_array(new_cap) # New bigger array
         
        for k in range(self.n): # Reference all existing values
            B[k] = self.A[k]
             
        self.A = B # Call A the fresh array
        self.capacity = new_cap # Reset the capacity
         
    def make_array(self,new_cap):
        """
        Returns a new array with new_cap capacity
        """
        return (new_cap * ctypes.py_object)()
    
array = OurOwnList()
array.append(115)
array.append(119)
array.append(12)
print(len(array))
print(array)
print(array.n)
print(array.capacity)
array.append(16)
array.append(16)
print(array.n)
print(array.capacity)