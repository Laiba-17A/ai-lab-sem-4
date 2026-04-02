# =========================
# UNIVERSAL ENVIRONMENT
# =========================
class Environment:
    def __init__(self, state):
        self.state = state

    def get_percept(self):
        return self.state


# =========================
# SIMPLE REFLEX AGENT
# =========================
class SimpleReflexAgent:
    def act(self, percept):
        if percept == "Dirty":
            return "Clean the room"
        return "No action needed"


# =========================
# MODEL BASED AGENT
# =========================
class ModelBasedAgent:
    def __init__(self):
        self.model = {}

    def update_model(self, percept):
        self.model["current"] = percept

    def act(self, percept):
        self.update_model(percept)

        if self.model["current"] == "Dirty":
            return "Clean"
        return "No action"


# =========================
# GOAL BASED AGENT
# =========================
class GoalBasedAgent:
    def __init__(self):
        self.goal = "Clean"

    def act(self, percept):
        if percept == "Dirty":
            self.goal = "Clean"
            return "Clean room"
        else:
            self.goal = "Done"
            return "Goal achieved"


# =========================
# UTILITY BASED AGENT
# =========================
class UtilityBasedAgent:
    def __init__(self):
        self.utility = {"Dirty": -10, "Clean": 10}

    def calculate_utility(self, percept):
        return self.utility[percept]

    def act(self, percept):
        if percept == "Dirty":
            return "Clean room"
        return "No action"


# =========================
# LEARNING AGENT
# =========================
class LearningAgent:
    def __init__(self):
        self.memory = {}

    def learn(self, state, reward):
        self.memory[state] = reward

    def act(self, percept):
        if percept == "Dirty":
            self.learn(percept, 10)
            return "Clean"
        return "No action"


# =========================
# UNIVERSAL RUN FUNCTION
# =========================
def run_agent(agent, environment, steps=1):
    for step in range(steps):
        percept = environment.get_percept()
        action = agent.act(percept)

        print(f"Step {step + 1}")
        print("Percept:", percept)
        print("Action:", action)
        print("-" * 30)


# =========================
# MAIN PROGRAM
# =========================
env = Environment("Dirty")

print("=== Simple Reflex Agent ===")
run_agent(SimpleReflexAgent(), env)

print("=== Model Based Agent ===")
run_agent(ModelBasedAgent(), env)

print("=== Goal Based Agent ===")
run_agent(GoalBasedAgent(), env)

print("=== Utility Based Agent ===")
run_agent(UtilityBasedAgent(), env)

print("=== Learning Agent ===")
run_agent(LearningAgent(), env)