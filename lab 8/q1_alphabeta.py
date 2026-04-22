import math

class Node:
    def __init__(self, value=None):
        self.value = value
        self.children = []
        self.minmax_value = None

class MinimaxAgent:
    def __init__(self, depth):
        self.depth = depth

    def formulate_goal(self, node):
        return "Goal reached" if node.minmax_value is not None else "Searching"

    def act(self, node, environment):
        goal_status = self.formulate_goal(node)
        if goal_status == "Goal reached":
            return f"Minimax value for root node: {node.minmax_value}"
        else:
            return environment.alpha_beta_search(node, self.depth, -math.inf, math.inf, False)

class Environment:
    def __init__(self, tree):
        self.tree = tree
        self.computed_nodes = []

    def get_percept(self, node):
        return node

    def alpha_beta_search(self, node, depth, alpha, beta, maximizing_player=False):
        self.computed_nodes.append(node.value)
        if depth == 0 or not node.children:
            return node.value

        if maximizing_player:
            value = -math.inf
            for child in node.children:
                value = max(value, self.alpha_beta_search(child, depth - 1, alpha, beta, False))
                alpha = max(alpha, value)
                if beta <= alpha:
                    print("Pruned node:", child.value)
                    break
            node.minmax_value = value
            return value
        else:
            value = math.inf
            for child in node.children:
                value = min(value, self.alpha_beta_search(child, depth - 1, alpha, beta, True))
                beta = min(beta, value)
                if beta <= alpha:
                    print("Pruned node:", child.value)
                    break
            node.minmax_value = value
            return value

def run_agent(agent, environment, start_node):
    percept = environment.get_percept(start_node)
    agent.act(percept, environment)

root = Node('A')

n1 = Node('B')
n2 = Node('C')
root.children = [n1, n2]

n3 = Node('D')
n4 = Node('E')
n5 = Node('F')
n6 = Node('G')
n7 = Node('H')
n1.children = [n3, n4]
n2.children = [n5, n6, n7]


nI  = Node(5)
nJ  = Node(7)
nK  = Node(1)
nL  = Node(9)
nM  = Node(2)
nN  = Node(5)
nO  = Node(10)
nP  = Node(12)
nQ  = Node(6)
nR  = Node(20)

n3.children = [nI, nJ, nK]
n4.children = [nL, nM]
n5.children = [nN, nO]
n6.children = [nP, nQ]
n7.children = [nR]

depth = 3
agent = MinimaxAgent(depth)
environment = Environment(root)
run_agent(agent, environment, root)

print("Computed Nodes:", environment.computed_nodes)
print("Minimax values:")
print(f"A: {root.minmax_value}")
print(f"B: {n1.minmax_value}")
print(f"C: {n2.minmax_value}")
print(f"D: {n3.minmax_value}")
print(f"E: {n4.minmax_value}")
print(f"F: {n5.minmax_value}")
print(f"G: {n6.minmax_value}")
print(f"H: {n7.minmax_value}")