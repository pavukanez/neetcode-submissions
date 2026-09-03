class TimeMap:

    def __init__(self):
        self.records = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.records:
            self.records[key] = []

        self.records[key].append((timestamp, value))
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.records:
            return ""
        
        arr = self.records[key]

        l, r = 0, len(arr) - 1
        res = ""

        while l <= r:
            m = l + (r - l) // 2

            if arr[m][0] <= timestamp:
                res = arr[m][1]
                l = m + 1
            else:
                r = m - 1
        return res
        
