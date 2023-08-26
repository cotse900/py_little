class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key = lambda x: x[1])
        chain = 0
        current_end = -1001
        for pair in pairs:
            if pair[0] > current_end:
                chain += 1
                current_end = pair[1]
        return chain
