class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt = Counter(tasks)
        # To track the tasks need to be processed
        # The most frequent tasks at the top
        max_heap = [-c for c in cnt.values()]
        heapq.heapify(max_heap)
        
        time = 0
        q = deque()  # [-cnt, idleTime]
        
        while max_heap or q:
            time += 1
            
            # No task is available to process at this moment, thus update the current time
            if not max_heap:
                time = q[0][1]
            else:
                cnt = 1 + heapq.heappop(max_heap)
                # The task needs to be rescheduled
                if cnt != 0:
                    q.append([cnt, time + n])
            
            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.popleft()[0])
        
        return time