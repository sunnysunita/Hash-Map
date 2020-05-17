
class MapNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class Map:
    def __init__(self):
        self.bucket_size = 10
        self.bucket = [None for i in range(self.bucket_size)]
        self.count = 0


    def size(self):
        return self.count

    def get_index(self,key):
        return abs(hash(key))%self.bucket_size

    def insert(self, key, value):
        index = self.get_index(key)
        head = self.bucket[index]
        while head is not None:
            if head.key == key:
                head.value = value
                return
            head = head.next

        new_node = MapNode(key, value)
        new_node.next = head
        self.bucket[index] = new_node
        self.count += 1

m = Map()
print(m.size())
m.insert("sunny", 79)
print(m.size())
m.insert("arun", 80)
print(m.size())
m.insert("arun", 100)
print(m.size())