# biDirectional BFS search for shortest path
# Leetcode: https://leetcode.com/problems/word-ladder/

# The idea here is to create two queues for a BFS search to get the shortest path
# and find the amount of steps it takes for the two queues to meet (one at beginning, one at end). 
# This is in practice exponentially faster than a typical BFS djikstra algorithm. 

from collections import deque, defaultdict

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or beginWord == endWord:
            return 0
        adj = defaultdict(list)

        for word in wordList + [beginWord]:
            for i in range(len(word)):
                adj[word[0:i] + '*' + word[i+1:]].append(word)

        
        def bfs():
            nonlocal beginWord, endWord
            q1, q2 = deque(), deque()
            q1.append(beginWord)
            q2.append(endWord)
            visit1, visit2 = {beginWord}, {endWord}
            steps = 1

            while q1 and q2:
                # Keep q1 smaller so we expand smaller
                if len(q1) > len(q2):
                    q1, q2 = q2, q1
                    visit1, visit2 = visit2, visit1

                # Pop q1 a level
                for _ in range(len(q1)):
                    node1 = q1.popleft()
                    for i in range(len(node1)):
                        pattern = node1[:i] + '*' + node1[i+1:]
                        for nei in adj[pattern]:
                            if nei in visit2:
                                return steps + 1
                            if nei not in visit1:
                                q1.append(nei)
                                visit1.add(nei)
                steps += 1
            return 0 

        return bfs()
