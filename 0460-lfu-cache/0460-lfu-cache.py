class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
        self.freq = 1
class LL:
    def __init__(self):
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.len = 0

    def add(self,node):
        node.next =self.head.next
        self.head.next.prev = node
        self.head.next = node
        node.prev = self.head
        self.len +=1
    
    def remove(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = None
        node.prev = None
        self.len -=1

    def removelast(self):
        last = self.tail.prev
        self.remove(last)
        return last

class LFUCache(object):

    def __init__(self, capacity):
        self.freqlist = defaultdict(LL)
        self.d = {}
        self.c = capacity
        self.min_f = 1

    def get(self, key):
        if key in self.d:
            node = self.d[key]
            self.update(key)
            return node.val
        return -1
        

    def put(self, key, value):
        if not self.c:
            return 
        if key in self.d:
            node = self.d[key]
            node.val = value
            self.update(key)
        else:
            if len(self.d) == self.c:
                k = self.freqlist[self.min_f].removelast().key
                del self.d[k]
            node = Node(key,value)
            self.d[key] = node
            self.freqlist[1].add(node)
            self.min_f =1

    def update(self,key):  
        node = self.d[key]
        p_f = node.freq
        node.freq+=1
        self.freqlist[p_f].remove(node)
        self.freqlist[node.freq].add(node)
        if p_f == self.min_f and not self.freqlist[self.min_f].len:
            self.min_f+=1


