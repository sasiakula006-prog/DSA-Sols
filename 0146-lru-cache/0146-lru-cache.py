class Node():
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next =  None
        self.prev = None
class LRUCache(object):

    def __init__(self, capacity):
        self.d = {}
        self.c = capacity
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = None
        node.prev = None

    def add(self,node):
        self.head.next.prev = node
        node.next = self.head.next
        self.head.next = node
        node.prev = self.head
        

    def get(self, key):
        if key in self.d:
            node = self.d[key]
            self.remove(node)
            self.add(node)
            return node.value
        return -1
        

    def put(self, key, value):
        if key in self.d:
            node = self.d[key]
            node.value = value
            self.remove(node)
            self.add(node)           
        else:
            node = Node(key,value)
            self.add(node)
            self.d[key] = node
            if len(self.d) > self.c:
                a = self.tail.prev
                self.remove(a)
                del self.d[a.key]

        


