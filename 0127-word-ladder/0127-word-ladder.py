class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        from collections import deque
        q=deque([(beginWord,0)])
        l=[]
        wl=set(wordList)
        for w in wordList:
            for i in w:
                if i not in l:
                    l.append(i)
        v=set()
        v.add(beginWord)
        while q:
            k,c=q.popleft()
            if k==endWord:
                return c+1
            for i in range(len(k)):
                for j in l:
                    nw=k[:i]+j+k[i+1:]
                    if nw not in v and nw in wl:
                        print(nw)
                        v.add(nw)
                        q.append((nw,c+1))
        return 0 