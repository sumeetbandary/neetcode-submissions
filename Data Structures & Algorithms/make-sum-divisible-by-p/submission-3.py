from typing import List

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        target = total % p

        # Already divisible by p
        if target == 0:
            return 0

        # remainder -> latest index
        seen = {0: -1}

        prefix = 0
        result = len(nums)

        for i, num in enumerate(nums):
            prefix = (prefix + num) % p

            # We need:
            # (prefix - previous_prefix) % p == target
            #
            # previous_prefix = (prefix - target) % p
            required = (prefix - target) % p

            if required in seen:
                result = min(result, i - seen[required])

            # Store latest index
            seen[prefix] = i

        # Cannot remove the entire array
        if result == len(nums):
            return -1

        return result