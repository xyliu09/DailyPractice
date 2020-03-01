class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        ans = []

        def allValidSuffix(word):
            validSuffix = set()
            for i in range(len(word)):
                if word[:i + 1] == word[:i + 1][::-1]:
                    validSuffix.add(word[i + 1:])
            return validSuffix

        def allValidPrefix(word):
            validPrefix = set()
            for i in range(len(word)):
                if word[i:] == word[i:][::-1]:
                    validPrefix.add(word[:i])
            return validPrefix

        word_to_look_up = {word: i for i, word in enumerate(words)}

        for i, word in enumerate(words):
            reverse = word[::-1]

            if reverse in word_to_look_up and reverse != word:
                ans.append([word_to_look_up[reverse], i])
            for suffix in allValidSuffix(word):
                reverse_suffix = suffix[::-1]
                if reverse_suffix in word_to_look_up:
                    ans.append([word_to_look_up[reverse_suffix], i])
            for prefix in allValidPrefix(word):
                reverse_prefix = prefix[::-1]
                if reverse_prefix in word_to_look_up:
                    ans.append([i, word_to_look_up[reverse_prefix]])
        return ans
