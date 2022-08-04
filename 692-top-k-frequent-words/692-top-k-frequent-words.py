import collections, heapq


class lexOrder:
    def __init__(self, word):
        self.word = word
    
    def __lt__(self, other):
        return self.word > other.word

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = collections.Counter(words)
        heap = []
        for word,freq in counter.items():
            heapq.heappush(heap, (freq, lexOrder(word)))
            if len(heap) > k:
                heapq.heappop(heap)
        output = []
        while heap:
            _freq, reverseWordObj = heapq.heappop(heap)
            output.append(reverseWordObj.word)
        return output[::-1]