
class Environment:
    def __init__(self):
        self.rocks = {
            "Rock A": {"value": 5, "cost": 2},
            "Rock B": {"value": 9, "cost": 8},
            "Rock C": {"value": 6, "cost": 3}
        }

    def get_percept(self):
        return self.rocks


class UtilityBasedAgent:
    def utility(self, value, cost):
        return (value * 2) - cost

    def act(self, rocks):
        best_rock = None
        best_score = -999

        for rock, data in rocks.items():
            score = self.utility(data["value"], data["cost"])

            if score > best_score:
                best_score = score
                best_rock = rock

        return best_rock


def run_agent(agent, environment):
    rocks = environment.get_percept()
    best = agent.act(rocks)
    print("Best rock:", best)


agent = UtilityBasedAgent()
environment = Environment()
run_agent(agent, environment)

''' 
A Mars Rover is stationary and needs to select the best rock for sampling 
based on limited battery life and scientific return, acting as a utility-based 
agent. You are provided with three target rocks: Rock A (Value: 5, Cost: 2), 
Rock B (Value: 9, Cost: 8), and Rock C (Value: 6, Cost: 3). You must implement 
a script that calculates a utility score for each rock using the formula 
(Mineral Value * 2) - Energy Cost, compares the results, and outputs the name of 
the rock with the highest calculated utility score.

'''