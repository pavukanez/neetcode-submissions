class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1
        
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, count in freq.items():
            buckets[count].append(num)

        res = []
        for i in range(len(buckets) - 1, -1, -1):
            if not buckets[i] or k <= 0:
                continue
            idx = 0
            while k > 0 and idx < len(buckets[i]):
                res.append(buckets[i][idx])
                idx += 1
                k -= 1
        return res
        