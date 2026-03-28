
'''Question 3: India vs. Pakistan (The Bunker Raid)
Tensions have exploded on the border! An Indian special ops team is raiding a secret
underground bunker in Pakistan to locate a server labeled 'Target'. The bunker is a maze of
rooms, but the soldiers have limited oxygen tanks that only allow them to go 2 levels deep.
Graph:
● 'Entrance' (Level 0) connects to ['Hallway_A', 'Hallway_B']
● 'Hallway_A' (Level 1) connects to ['Storage'] (Level 2)
● 'Hallway_B' (Level 1) connects to ['Target'] (Level 2)
● 'Storage' connects to ['Deep_Vault'] (Level 3 - Too Deep!)
Task: Write a Python program using DLS with a limit=2. Start at 'Entrance'. If you reach
the limit without finding the target, the code must backtrack. If 'Target' is found within the
limit, print "Mission Accomplished!"'''


# Goal-Based Agent (DLS)
class GoalBasedAgent:
    def __init__(self, goal, depth_limit):
        self.goal = goal
        self.depth_limit = depth_limit

    def dls_search(self, graph, node, depth, visited):
        print(f"Visiting: {node}, Depth: {depth}")

        # Goal check
        if node == self.goal:
            return "Mission Accomplished!"

        # Depth limit check
        if depth == self.depth_limit:
            return None

        visited.append(node)

        # Explore neighbors
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                result = self.dls_search(graph, neighbor, depth + 1, visited)
                if result:
                    return result

        visited.pop()  # backtracking
        return None

    def act(self, percept, graph):
        result = self.dls_search(graph, percept, 0, [])
        return result if result else "Target not found within depth limit"


# Environment
class Environment:
    def __init__(self, graph):
        self.graph = graph

    def get_percept(self, node):
        return node


# Run Agent
def run_agent(agent, env, start):
    percept = env.get_percept(start)
    result = agent.act(percept, env.graph)
    print(result)


# Graph (Bunker Layout)
graph = {
    'Entrance': ['Hallway_A', 'Hallway_B'],
    'Hallway_A': ['Storage'],
    'Hallway_B': ['Target'],
    'Storage': ['Deep_Vault'],
    'Target': [],
    'Deep_Vault': []
}

# Create Agent + Environment
agent = GoalBasedAgent(goal='Target', depth_limit=2)
env = Environment(graph)

# Run
run_agent(agent, env, 'Entrance')