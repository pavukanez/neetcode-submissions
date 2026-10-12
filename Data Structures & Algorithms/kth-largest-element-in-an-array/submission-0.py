class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minNum, maxNum = min(nums), max(nums)

        arr = [0] * (maxNum - minNum + 1)

        counter = Counter(nums)

        for num, count in counter.items():
            arr[num - minNum] = count

        for i in range(len(arr) - 1, -1, -1):
            if arr[i] == 0:
                continue
            
            while k > 0 and arr[i] > 0:
                k -= 1
                arr[i] -= 1
            
            if k == 0:
                return i + minNum

        return 0

