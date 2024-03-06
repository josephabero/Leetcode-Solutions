"""
Course Schedule
https://leetcode.com/problems/course-schedule
"""
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Initialize adjacency list
        course_list = {i:[] for i in range(numCourses)}

        # Fill out adjacency list
        for course, prereq in prerequisites:
            course_list[course].append(prereq)

        # Keep set of visited course to detect cycle
        visited = set()
        def dfs(course):
        	# Cycle found
            if course in visited:
                return False

            # Empty prerequisites
            if not course_list[course]:
                return True

            visited.add(course)
            # Traverse adjacency list
            for prereq in course_list[course]:
                if not dfs(prereq):
                    return False
            visited.remove(course)

            # Label course as completed prerequisites
            course_list[course] = []

            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True

