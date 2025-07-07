from heapq import heappush, heappop

class Solution:
    def maxEvents(self, events: list[list[int]]) -> int:
        events.sort() #sort by earliest start time
        
        latestDay : int = max(events[0])
        for event in events:
            latestDay = max(latestDay, max(event))
        
        minHeap = []
        i : int = 0
        day : int = 1
        count : int = 0

        while day <= latestDay:
            if not minHeap and i < len(events):
                day = max(day, events[i][0])

            # Remove past events
            while minHeap and minHeap[0] < day:
                heappop(minHeap)

            # Add events starting today
            while i < len(events) and events[i][0] == day:
                heappush(minHeap, events[i][1])
                i += 1

            # Attend the event that ends earliest
            if minHeap:
                heappop(minHeap)
                count += 1
            elif i == len(events):  # No more events to process
                break

            day += 1
        return count




solution : Solution = Solution()
print(solution.maxEvents([[1,2], [2,3], [3,4]])) # 3
print(solution.maxEvents([[1,2], [2,3], [3,4], [1,2]])) # 4
print(solution.maxEvents([[1,2], [1,3], [2,4], [3,4], [4,5]])) # 6