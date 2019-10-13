
class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []
        self.table = {}

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.table:
            self.table[val] = len(self.data)
            self.data.append(val)
            return True
        return False

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.table:
            self.table[self.data[-1] ]= self.table[val]
            self.data[self.table[self.data[-1]]], self.data[-1] = self.data[-1], self.data[self.table[self.data[-1]]]
            del self.table[val]
            self.data.pop()
            return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        index = random.randint(0 ,len(self.data ) -1)
        return self.data[index]



        # Your RandomizedSet object will be instantiated and called as such:
        # obj = RandomizedSet()
        # param_1 = obj.insert(val)
        # param_2 = obj.remove(val)
        # param_3 = obj.getRandom()