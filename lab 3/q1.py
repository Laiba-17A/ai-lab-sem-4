import random


# Environment Class
class Environment:
    def __init__(self):
        # Task A: random initial state
        self.state = random.choice(["Dirty", "Clean"])

    def get_percept(self):
        return self.state

    def clean_room(self):
        self.state = "Clean"

    # Task B: random state after each step
    def change_state_randomly(self):
        self.state = random.choice(["Dirty", "Clean"])


# Agent Class
class SimpleReflexAgent:
    def __init__(self):
        pass

    def act(self, percept):
        if percept == "Dirty":
            return "Clean the room"
        else:
            return "Room is already clean"


# Simulation Function
def run_agent(agent, environment, steps):
    for step in range(steps):
        percept = environment.get_percept()
        action = agent.act(percept)

        print(f"Step {step + 1}: Percept = {percept}, Action = {action}")

        if percept == "Dirty":
            environment.clean_room()

        # Task B: environment changes randomly after every step
        environment.change_state_randomly()


# Create objects
agent = SimpleReflexAgent()
environment = Environment()

# Run simulation
run_agent(agent, environment, 5)