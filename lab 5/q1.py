

'''TASK #1
Enhanced Maze Navigation with Multiple Goals
● Description: Modify the given Best-First Search to find a path through a maze
with multiple goal points. The algorithm should visit all goal points and return
the shortest path covering all goals.
● Challenge: The maze will have several dead ends and multiple goal points at
different locations.'''

from queue import PriorityQueue

# Heuristic (Manhattan Distance)
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


# Agent
class GoalBasedAgent:
    def __init__(self, goals):
        self.goals = goals

    def best_first_search(self, maze, start, goal):
        rows, cols = len(maze), len(maze[0])
        pq = PriorityQueue()
        pq.put((0, start))
        came_from = {start: None}
        visited = set()

        while not pq.empty():
            _, current = pq.get()

            if current == goal:
                path = []
                while current:
                    path.append(current)
                    current = came_from[current]
                return path[::-1]

            visited.add(current)

            for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                nx, ny = current[0]+dx, current[1]+dy

                if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 0:
                    neighbor = (nx, ny)

                    if neighbor not in visited:
                        priority = heuristic(neighbor, goal)
                        pq.put((priority, neighbor))
                        came_from[neighbor] = current

        return None

    def act(self, percept, maze):
        current = percept
        full_path = []

        for goal in self.goals:
            print(f"Finding path to goal: {goal}")
            path = self.best_first_search(maze, current, goal)

            if path:
                full_path.extend(path[1:])
                current = goal
            else:
                return "Goal unreachable"

        return f"Path covering all goals: {full_path}"


# Environment
class Environment:
    def __init__(self, maze):
        self.maze = maze

    def get_percept(self, start):
        return start


# Run
def run_agent(agent, env, start):
    percept = env.get_percept(start)
    result = agent.act(percept, env.maze)
    print(result)


# Maze (0 = open, 1 = wall)
maze = [
    [0,0,1,0,0],
    [0,0,0,0,0],
    [0,0,1,0,1],
    [0,0,0,0,0],
    [0,1,0,0,0]
]

goals = [(0,4), (4,4)]  # multiple goals

agent = GoalBasedAgent(goals)
env = Environment(maze)

run_agent(agent, env, (0,0))