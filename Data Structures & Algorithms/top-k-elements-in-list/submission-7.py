class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        
        res = [[] for _ in range(len(nums) + 1)]

        for key, val in count.items():
            res[val].append(key)

        output = []
        # [[], [1], [2], [3]]
        for i in range(len(res) - 1, 0, -1):
            arr = res[i]
            for num in arr:
                output.append(num)
                k -= 1
                if k == 0:
                    return output
        

        