class RandomizedSet(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic, self.ds = {}, []

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.dic:
            self.ds.append(val)
            self.dic[val] = len(self.ds) - 1
            return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.dic:
            idx, last = self.dic[val], self.ds[-1]
            self.ds[idx], self.dic[last] = last, idx
            del self.dic[val]
            del self.ds[-1]
            return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return self.ds[random.randint(0, len(self.ds) - 1)]



        # Your RandomizedSet object will be instantiated and called as such:
        # obj = RandomizedSet()
        # param_1 = obj.insert(val)
        # param_2 = obj.remove(val)
        # param_3 = obj.getRandom()