

class Environment:
    def __init__(self):
        self.houses = [
            "Blue House", "Green House", "Red House",
            "Yellow House", "White House"
        ]

    def get_percept(self, step):
        return self.houses[step]


class GoalBasedAgent:
    def __init__(self):
        self.goal = "Red House"

    def act(self, house):
        if house == self.goal:
            return "Target found"
        return "Keep searching"


def run_agent(agent, environment):
    for i in range(len(environment.houses)):
        house = environment.get_percept(i)
        action = agent.act(house)
        print(house, "->", action)

        if house == agent.goal:
            break


agent = GoalBasedAgent()
environment = Environment()
run_agent(agent, environment)

''' 
Develop a control system for a delivery drone that operates as a goal-based 
agent tasked with finding a specific drop-off location, the "Red House," 
within a neighborhood represented by the list ['Blue House', 'Green House', 
'Red House', 'Yellow House', 'White House']. The drone must fly to each 
house in the list sequentially and check if the current location matches its 
goal; if the house is not the target, it should continue, but the moment it 
reaches the "Red House," it must print a success message and immediately 
terminate the mission without visiting the remaining houses to demonstrate efficiency.
'''