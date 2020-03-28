class TrieNode():
    def __init__(self):
        self.children = [None] * 27
        self.freq = {}


class AutocompleteSystem:
    def __init__(self, sentences: List[str], times: List[int]):
        self.root = TrieNode()
        self.cur = None
        self.string = ''
        for i in range(len(sentences)):
            self.insert(sentences[i], times[i])

    def insert(self, sentence, count):
        node = self.root
        for i in range(len(sentence)):
            index = 26 if sentence[i] == ' ' else ord(sentence[i]) - ord('a')
            if not node.children[index]:
                node.children[index] = TrieNode()
            node = node.children[index]
            node.freq[sentence] = node.freq.get(sentence, 0) + count

    def findTopK(self):
        node = self.cur
        heap = []
        res = []
        for sentence, freq in node.freq.items():
            heapq.heappush(heap, (-freq, sentence))
        while heap and (not res or len(res) < 3):
            res.append(heapq.heappop(heap)[1])
        return res

    def input(self, c):
        if not self.cur:
            self.cur = self.root

        if c == "#":
            self.insert(self.string, 1)
            self.cur = None
            self.string = ''
            return []

        self.string += c
        index = 26 if c == ' ' else ord(c) - ord('a')
        if not self.cur.children[index]:
            self.cur.children[index] = TrieNode()
        self.cur = self.cur.children[index]

        return self.findTopK()


        # Your AutocompleteSystem object will be instantiated and called as such:
        # obj = AutocompleteSystem(sentences, times)
        # param_1 = obj.input(c)