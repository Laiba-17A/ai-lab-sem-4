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
        return "goal reached" if node.minmax_value is not None else "searching"

    def act(self, node, env):
        status = self.formulate_goal(node)
        if status == "goal reached":
            return f"minimax value for root: {node.minmax_value}"
        else:
            return env.alpha_beta_search(node, self.depth, -math.inf, math.inf, True)

class Environment:
    def __init__(self, tree):
        self.tree = tree
        self.computed = []

    def get_percept(self, node):
        return node

    def alpha_beta_search(self, node, depth, alpha, beta, is_max=True):
        self.computed.append(node.value)
        if depth == 0 or not node.children:
            return node.value

        if is_max:
            val = -math.inf
            for child in node.children:
                val = max(val, self.alpha_beta_search(child, depth - 1, alpha, beta, False))
                alpha = max(alpha, val)
                if beta <= alpha:
                    print("pruned:", child.value)
                    break
            node.minmax_value = val
            return val
        else:
            val = math.inf
            for child in node.children:
                val = min(val, self.alpha_beta_search(child, depth - 1, alpha, beta, True))
                beta = min(beta, val)
                if beta <= alpha:
                    print("pruned:", child.value)
                    break
            node.minmax_value = val
            return val

def run_agent(agent, env, start):
    percept = env.get_percept(start)
    agent.act(percept, env)

def sort_branches(tree):
    for i in range(len(tree)):
        for j in range(i + 1, len(tree)):
            if max(tree[j]) > max(tree[i]):
                tree[i], tree[j] = tree[j], tree[i]
    return tree

def build_tree(branches):
    labels = ['cyber attack', 'signal jamming', 'market crash']
    root = Node('root')
    for i, scores in enumerate(branches):
        branch = Node(labels[i])
        for s in scores:
            branch.children.append(Node(s))
        root.children.append(branch)
    return root

def alpha_beta_defense(tree):
    sorted_tree = sort_branches(tree)

    print("original:", tree)
    print("sorted  :", sorted_tree)
    print()

    root = build_tree(sorted_tree)
    depth = 2
    agent = MinimaxAgent(depth)
    env = Environment(root)
    run_agent(agent, env, root)

    print("computed:", env.computed)
    print("values  :")
    for child in root.children:
        print(f"  {child.value}: {child.minmax_value}")
    print(f"  root: {root.minmax_value}")

    return root.minmax_value

tree = [[10, 5, 2], [8, 4, 3], [20, 15, 9]]
result = alpha_beta_defense(tree)
print("\noptimal defense score:", result)