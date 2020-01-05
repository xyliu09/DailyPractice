from collections import Counter, deque
class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> \
    List[str]:
        visited, bfs = {id}, {id}
        for _ in range(level):
            bfs = {j for i in bfs for j in friends[i] if j not in visited}
            visited |= bfs
        freq = Counter([x for idx in bfs for x in watchedVideos[idx]])
        return sorted(freq.keys(), key=lambda x: (freq[x], x))