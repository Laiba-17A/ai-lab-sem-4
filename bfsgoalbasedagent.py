
# Goal-Based Agent Class
class GoalBasedAgent:
    def __init__(self, goal):
        self.goal = goal   # store goal node

    # check if current percept is goal
    def formulate_goal(self, percept):
        if percept == self.goal:
            return "Goal reached"
        return "Searching"

    # BFS Search
    def bfs_search(self, graph, start, goal):
        visited = []
        queue = [(start, [start])]   # store node + path

        while queue:
            node, path = queue.pop(0)   # dequeue first node
            print("Visiting:", node)

            # goal test
            if node == goal:
                return "Goal found! Path = " + str(path)

            if node not in visited:
                visited.append(node)

                # add neighbours
                for neighbour in graph.get(node, []):
                    queue.append((neighbour, path + [neighbour]))

        return "Goal not found"

    # decide action
    def act(self, percept, graph):
        status = self.formulate_goal(percept)

        if status == "Goal reached":
            return "Goal already reached"
        else:
            return self.bfs_search(graph, percept, self.goal)


# Environment Class
class Environment:
    def __init__(self, graph):
        self.graph = graph   # store graph

    def get_percept(self, node):
        return node


# Run Agent
def run_agent(agent, environment, start_node):
    percept = environment.get_percept(start_node)
    action = agent.act(percept, environment.graph)
    print(action)


# Tree Representation
tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': [],
    'F': ['I'],
    'G': [],
    'H': [],
    'I': []
}

# Start and Goal
start_node = 'A'
goal_node = 'I'

# Create objects
agent = GoalBasedAgent(goal_node)
environment = Environment(tree)

# Run
run_agent(agent, environment, start_node)