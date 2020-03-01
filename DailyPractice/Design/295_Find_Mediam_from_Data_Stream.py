import bisect


class MedianFinder(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.store = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        bisect.insort_left(self.store, num)

    def findMedian(self):
        """
        :rtype: float
        """
        if not self.store:
            return
        if len(self.store) % 2 == 0:
            return (self.store[(len(self.store) - 1) // 2] + self.store[(len(self.store) - 1) // 2 + 1]) / 2.0
        else:
            return self.store[(len(self.store) - 1) // 2]



            # Your MedianFinder object will be instantiated and called as such:
            # obj = MedianFinder()
            # obj.addNum(num)
            # param_2 = obj.findMedian()