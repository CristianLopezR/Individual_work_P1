class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        size=[]
        rep=0
        for i in words:
            if sorted(i) not in size:
                size.append(sorted(i))
            else:
                rep+=1
        return rep
