class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        in_degree = [0] * numCourses

        for src, dest in prerequisites:
            graph[src].append(dest)
            in_degree[dest] += 1
        q = deque()
        for node in range(numCourses):
            if in_degree[node] == 0:
                q.append(node)

        finished = 0
        while q:
            node = q.popleft()
            finished += 1
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    q.append(neighbor)

        return finished == numCourses
