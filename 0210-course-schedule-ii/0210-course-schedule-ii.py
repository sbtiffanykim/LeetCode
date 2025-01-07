class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        graph = {i: [] for i in range(numCourses)}
        in_degree = [0] * numCourses

        for dest, src in prerequisites:
            graph[src].append(dest)
            in_degree[dest] += 1
        
        q = deque()
        for num in range(numCourses):
            if in_degree[num] == 0:
                q.append(num)
        
        finish = []
        while q:
            cur = q.popleft()
            finish.append(cur)
            for neighbor in graph[cur]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    q.append(neighbor)
        
        return finish if len(finish) == numCourses else []