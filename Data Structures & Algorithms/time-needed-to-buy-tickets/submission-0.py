class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0

        while True:
            currentTickets = tickets.pop(0)
            currentTickets -= 1
            time += 1
            if k == 0:
                if currentTickets == 0:
                    return time
                tickets.append(currentTickets)
                k = len(tickets) - 1
            else:
                if currentTickets != 0:
                    tickets.append(currentTickets)
                k -= 1
        return time