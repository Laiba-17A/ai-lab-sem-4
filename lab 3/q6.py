
import random


class Environment:
    def __init__(self):
        self.states = ["Start", "Empty", "Cheese", "Trap"]
        self.rewards = {
            "Empty": -1,
            "Cheese": 10,
            "Trap": -10
        }

    def get_percept(self):
        return random.choice(self.states[1:])

    def get_reward(self, state):
        return self.rewards[state]


class LearningAgent:
    def act(self, percept):
        return percept


def run_agent(agent, environment):
    state = environment.get_percept()
    action = agent.act(state)
    reward = environment.get_reward(action)

    print("State:", state)
    print("Reward:", reward)


agent = LearningAgent()
environment = Environment()
run_agent(agent, environment)

''' 
Create a simulation for a basic learning agent represented as a mouse placed 
on a linear track containing four spots: Start, Empty, Cheese, and Trap. 
The environment assigns specific rewards to each location, where finding 
Cheese grants +10 points, hitting a Trap results in -10 points, and landing on 
an Empty spot deducts 1 point; the program should start the mouse at the first 
position, simulate a random move to one of the other spots, and print the resulting 
state and the specific reward received to demonstrate the concept of trial-and-error feedback.

'''