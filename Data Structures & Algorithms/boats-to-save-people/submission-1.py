class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        people.sort()
        left, right = 0, len(people) - 1
        boats = 0
        
        while left <= right:
            # If the lightest person and heaviest person can fit together
            if people[left] + people[right] <= limit:
                left += 1
            # The heaviest person always gets a boat
            right -= 1
            boats += 1
            
        return boats