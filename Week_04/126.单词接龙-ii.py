#
# @lc app=leetcode.cn id=126 lang=python3
#
# [126] 单词接龙 II
#

# @lc code=start
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        L = len(beginWord)
        hash=collections.defaultdict(list)
        # hash = {}
        for word in wordList:
            for i in range(L):
                hash[word[:i]+"*"+word[i+1:]].append(word)

        # 生成需要访问的路径队列
        # queue = [(beginWord, [beginWord])]
        queue = collections.deque()
        queue.append((beginWord, [beginWord]))
        # 生成已访问节点
        visited = set()
        visited.add(beginWord)
        # 保存结果
        res = []
        found = False
        while queue and not found:
            new_visited = set()
            # 依次输出队列中所有路径
            for _ in range(len(queue)):
                word, path = queue.popleft()
                # 如果当前节点是endWord，保存路径
                if word == endWord:
                    res.append(path)
                    found = True
                    continue
                # 访问该节点所有边
                for i in range(L):
                    masked_word = word[:i]+"*"+word[i+1:]
                    # 访问该节点通过这条边能够访问的所有节点
                    for j in hash[masked_word]:
                        # 因为是求最短路径，所以如果节点已经访问过则不再访问
                        if j not in visited:
                            queue.append((j, path + [j]))
                            new_visited.add(j)
            # 更新已经访问过的节点
            visited |= new_visited
        return res 
