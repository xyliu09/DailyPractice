class Solution(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.init = nums
        self.array = list(nums)

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        self.array = self.init
        self.init = list(self.init)
        return self.array

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        for i in range(len(self.array)):
            swap_index = random.randrange(i, len(self.array))
            self.array[i], self.array[swap_index] = self.array[swap_index], self.array[i]
        return self.array
        return res



        # Your Solution object will be instantiated and called as such:
        # obj = Solution(nums)
        # param_1 = obj.reset()
        # param_2 = obj.shuffle()