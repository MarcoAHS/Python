stock_prices = [['march 6', 310],
                ['march 7', 340],
                ['march 8', 380],
                ['march 9', 302],
                ['march 10', 297],
                ['march 11', 323],
                ['march 12', 340],
                ['march 21', 410],
                ['december 12', 320]]

def get_hash(key):
    h = 0
    for char in key:
        h+= ord(char)
    return h % 100

class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]
    
    def get_Hash(self, key):
        h = 0
        for char in key:
            h+=ord(char)
        return h % self.MAX
    
    def __setitem__(self, key, value):
        h = self.get_Hash(key)
        found = False
        for ind, ele in enumerate(self.arr[h]):
            if len(ele)==2 and ele[0] == key:
                self.arr[h][ind] = (key, value)
                found = True
                break
        if not found:
            self.arr[h].append((key, value))
    
    def __getitem__(self, key):
        h = self.get_Hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element

    def __delitem__(self, key):
        h = self.get_Hash(key)
        for ind, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][ind]

H = HashTable()
for i in range(len(stock_prices)):
    H.__setitem__(stock_prices[i][0], stock_prices[i][1])
print(H.arr)
del H['march 12']
print(H.arr)


    
