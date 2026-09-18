class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r)//2

            if target == nums[m]:
                return m
            
            # if it is left sorted portion
            if nums[l] <= nums[m]:
                # check the posibility of finding target in left sorted
                if target < nums[l] or target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1
            
            # right sorted portion
            else: 
                if target > nums[r] or target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            
        return -1

        