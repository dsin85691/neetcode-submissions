class DynamicArray:
    
    def __init__(self, capacity: int):
        self.array = [0] * capacity
        self.capacity = capacity
        self.length = 0 

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n 

    def pushback(self, n: int) -> None:
        if self.length == self.capacity: 
            self.resize() 
        self.array[self.length] = n  # Assign to the next available slot
        self.length += 1

    def popback(self) -> int:
        if self.length == 0:
            raise IndexError("Pop from empty array")
        self.length -= 1
        return self.array[self.length]  # Return the last valid element

    def resize(self) -> None:
        new_capacity = 2 * self.capacity
        new_array = [0] * new_capacity 

        for i in range(self.length):  # Copy only the valid elements
            new_array[i] = self.array[i]

        self.array = new_array
        self.capacity = new_capacity

    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return self.capacity