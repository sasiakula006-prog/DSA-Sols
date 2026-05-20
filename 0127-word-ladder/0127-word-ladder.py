class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        if endWord not in wordList or not endWord or not beginWord:
            return 0
        n = len(endWord)
        d = defaultdict(list)
        vis = set()
        q = deque()
        for word in wordList:
            for i in range(n):
                d[word[:i]+'*'+word[i+1:]].append(word)
        q.append((beginWord,1))
        vis.add(beginWord)
        while q:
            c_word,l = q.popleft()
            for i in range(n):
                possible_word = c_word[:i] + '*' + c_word[i+1:]
                for word in d[possible_word]:
                    if word == endWord:
                        return l+1
                    elif word not in vis:
                        q.append((word,l+1))
                        vis.add(word)
        return 0