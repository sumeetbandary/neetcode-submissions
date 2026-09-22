from collections import defaultdict

class TimeMap:

    def __init__(self):
        # Maps key -> list of [value, timestamp] pairs
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # Since timestamps are strictly increasing, appending keeps the list sorted
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.store.get(key, [])
        
        # Binary search to find the latest timestamp <= target timestamp
        left, right = 0, len(values) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if values[mid][1] <= timestamp:
                res = values[mid][0]  # Valid candidate found
                left = mid + 1        # Try finding a larger timestamp
            else:
                right = mid - 1       # Search left half
                
        return res