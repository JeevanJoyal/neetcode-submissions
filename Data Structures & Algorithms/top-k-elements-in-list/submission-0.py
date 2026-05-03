class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for num in nums: 
            if num in d: d[num] += 1
            else: d[num] = 1
        # print(d)
        heap = []
        heapq.heapify(heap)
        for key in d:
            heapq.heappush(heap, (-d[key], key))
        # print(heap)
        res = []
        while k: 
            res.append(heapq.heappop(heap)[1])
            k -= 1
        
        return res