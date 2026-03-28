
'''Question 2: Elon Musk’s Mission to Mars
Elon Musk has tasked you with programming the navigation for the first Starship flight from
'Earth' to 'Mars', but you must minimize the fuel cost to save billions of dollars. The flight network
has specific fuel costs: flying 'Earth' $\to$ 'Moon_Base' costs 10 fuel units, while 'Earth' $\to$
'Orbital_Platform' costs only 5 units. From the 'Orbital_Platform', you can take a highly efficient
shortcut to 'Moon_Base' for just 2 units, or fly a heavy route directly to 'Mars' for 60 units. Finally,
the 'Moon_Base' connects to 'Mars' for 50 units.
Task: Write a Python program using Uniform Cost Search (UCS). The agent must use a priority
queue to always explore the lowest-cost path first (comparing the cost of flying
Earth->Moon->Mars vs. Earth->Orbit->Moon->Mars) and output the cheapest path to the Red
Planet.'''

# Utility-Based Agent (UCS)
class UtilityBasedAgent:
    def __init__(self, goal):
        self.goal = goal

    def ucs_search(self, graph, start):
        frontier = [(start, 0)]  # (node, cost)
        visited = set()
        came_from = {start: None}

        while frontier:
            # sort by cost (priority queue behavior)
            frontier.sort(key=lambda x: x[1])
            node, cost = frontier.pop(0)

            if node in visited:
                continue

            print(f"Visiting: {node}, Cost: {cost}")
            visited.add(node)

            # Goal check
            if node == self.goal:
                path = []
                while node:
                    path.append(node)
                    node = came_from[node]
                path.reverse()

                return f"\nCheapest Path: {path}\nTotal Cost: {cost}"

            # Explore neighbors
            for neighbor, c in graph[node].items():
                if neighbor not in visited:
                    frontier.append((neighbor, cost + c))
                    came_from[neighbor] = node

        return "Goal not found"

    def act(self, percept, graph):
        return self.ucs_search(graph, percept)


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


# Graph (Fuel Cost Network)
graph = {
    'Earth': {'Moon_Base': 10, 'Orbital_Platform': 5},
    'Orbital_Platform': {'Moon_Base': 2, 'Mars': 60},
    'Moon_Base': {'Mars': 50},
    'Mars': {}
}

# Create Agent + Environment
agent = UtilityBasedAgent(goal='Mars')
env = Environment(graph)

# Run
run_agent(agent, env, 'Earth')