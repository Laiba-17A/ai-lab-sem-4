
'''Question 4: Pakistan vs. India (The Cyber-Attack at the World Cup)
During the final over of the Pakistan vs. India World Cup match, a cyber-attack cuts the stadium
lights! You are the Chief Engineer and must find the specific faulty switch labeled 'Breaker_101'
to restore power. The electrical grid is a hierarchy where the 'Main_Box' connects to 'Zone_A'
and 'Zone_B'; 'Zone_A' contains 'Switch_1' and 'Switch_2'; and 'Zone_B' contains the goal,
'Breaker_101'. Since you don't know how deep the problem is, you cannot search blindly; you
must check the shallow switches first before checking the deep ones.

Task: Write a Python program using Iterative Deepening Search (IDS). Use a loop to run a
search with limit=0, then limit=1, and finally limit=2. Print "Checking Depth X..." for each
iteration until 'Breaker_101' is found and the lights are back on.'''

def dls(graph, node, goal, depth):
    if depth == 0:
        return None

    if node == goal:
        return [node]

    for neighbor in graph.get(node, []):
        path = dls(graph, neighbor, goal, depth - 1)
        if path:
            return [node] + path

    return None


def ids(graph, start, goal, max_depth):
    for depth in range(max_depth + 1):
        print(f"Checking Depth {depth}...")
        path = dls(graph, start, goal, depth)

        if path:
            print("Goal Found:", path)
            return

    print("Goal not found")


graph = {
    'Main_Box': ['Zone_A', 'Zone_B'],
    'Zone_A': ['Switch_1', 'Switch_2'],
    'Zone_B': ['Breaker_101'],
    'Switch_1': [],
    'Switch_2': [],
    'Breaker_101': []
}

ids(graph, 'Main_Box', 'Breaker_101', 2)