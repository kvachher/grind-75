class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = {}
        for pair in prerequisites : 
            prv, nxt = pair[0], pair[1]
            if nxt not in adj_list:
                adj_list[nxt] = []
            if prv not in adj_list:
                adj_list[prv] = []
            adj_list[nxt].append(prv)
        def dfs(course, visited):
            if course in visited:
                return False
            prereqs = adj_list[course]
            if not prereqs:
                return True
            visited.add(course)
            while prereqs:
                prereq = prereqs.pop()
                if not dfs(prereq, visited):
                    return False
                if prereq in visited:
                    visited.remove(prereq)
            return True
        for course in adj_list:
            visited = set()
            if not dfs(course, set()):
                return False
        return True
