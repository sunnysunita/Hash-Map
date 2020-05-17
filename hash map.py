
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

        head = self.bucket[index]
        new_node = MapNode(key, value)
        new_node.next = head
        self.bucket[index] = new_node
        self.count += 1

    def remove(self, key):
        index = self.get_index(key)
        head = self.bucket[index]
        if head.key == key:
            x = head.value
            head = head.next
            self.bucket[index] = head
            self.count -= 1
            return x
        pre = None
        temp = head
        while head is not None:
            if head.key == key:
                pre.next = head.next
                head.next = None
                self.bucket[index] = temp
                self.count -= 1
                return head.value
            pre = head
            head = head.next
        return False

    def search(self, key):
        index = self.get_index(key)
        head = self.bucket[index]
        while head is not None:
            if head.key == key:
                return head.value
            head = head.next
        return None
m = Map()
print(m.size())
m.insert("sunny", 79)
print(m.size())
m.insert("arun", 80)
print(m.size())
m.insert("arun", 100)
print(m.size())
m.insert("ram", 800)
m.insert("shyam", 180)
m.insert("varun", 980)
m.insert("satyam", 80)
print(m.size())
print(m.search("sunny"))
print(m.remove("sunny"))
print(m.search("sunny"))

