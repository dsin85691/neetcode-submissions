class MyHashMap:

    def __init__(self):
        self.hash_map = {} 

    def put(self, key: int, value: int) -> None:
        self.hash_map[key] = value 

    def get(self, key: int) -> int:
        return self.hash_map[key] if key in self.hash_map else -1

    def remove(self, key: int) -> None:
        if key in self.hash_map:
            self.hash_map.pop(key)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)