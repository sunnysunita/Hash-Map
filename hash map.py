class MapNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None



class Map:
    def __init__(self):
        self.bucketsize = 10
        self.bucket = [None for i in range(self.bucketsize)]
        self.count = 0

    def size(self):
        return self.count


    def get_index(self, key):
        return abs(hash(key)) % self.bucketsize


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
        head = new_node
        self.bucket[index] = head
        self.count += 1
        return

    def search(self, key):
        index = self.get_index(key)
        head = self.bucket[index]
        while head is not None:
            if head.key == key:
                return head.value
            head = head.next
        return None

    def remove(self, key):
        index = self.get_index(key)
        head = self.bucket[index]
        pre = None
        while head is not None:
            if head.key == key:
                if pre == None:
                    head = head.next
                    self.bucket[index] = head
                    self.count -= 1
                    return True
                else:
                    pre = head.next
                    head.next = None
                    self.count -= 1
                    return True
            pre = head
            head = head.next
        return False


m = Map()
m.insert("abc", 100)
m.insert("abd", 200)
m.insert("abe", 300)
m.insert("abf", 400)
m.insert("abg", 500)
m.insert("abh", 600)
m.insert("abi", 700)
print(m.size())
print(m.search("abi"))
print(m.remove("abi"))
print(m.search("abi"))
print(m.size())
print(m.insert("abc",1000))
print(m.size())