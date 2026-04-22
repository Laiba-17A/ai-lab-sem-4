
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
            return environment.compute_minimax(node, self.depth)

class Environment:
    def __init__(self, tree):
        self.tree = tree
        self.computed_nodes = []

    def get_percept(self, node):
        return node

    def compute_minimax(self, node, depth, maximizing_player=False):
        if depth == 0 or not node.children:
            self.computed_nodes.append(node.value)
            return node.value

        if maximizing_player:
            value = -math.inf
            for child in node.children:
                child_value = self.compute_minimax(child, depth - 1, False)
                value = max(value, child_value)
            node.minmax_value = value
            self.computed_nodes.append(node.value)
            return value
        else:
            value = math.inf
            for child in node.children:
                child_value = self.compute_minimax(child, depth - 1, True)
                value = min(value, child_value)
            node.minmax_value = value
            self.computed_nodes.append(node.value)
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
print("A:", root.minmax_value)
print("B:", n1.minmax_value)
print("C:", n2.minmax_value)
print("D:", n3.minmax_value)
print("E:", n4.minmax_value)
print("F:", n5.minmax_value)
print("G:", n6.minmax_value)
print("H:", n7.minmax_value)