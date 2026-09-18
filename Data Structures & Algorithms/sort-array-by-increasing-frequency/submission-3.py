class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        # Step 1: Count how many times each number appears
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        # Step 2: Define the custom rule function
        def custom_sort_rule(x):
            # Sort by frequency ascending (freq[x]), 
            # then by number value descending (-x)
            return (freq[x], -x)

        # Step 3: Pass the function name directly as the sorting key
        nums.sort(key=custom_sort_rule)
        return nums