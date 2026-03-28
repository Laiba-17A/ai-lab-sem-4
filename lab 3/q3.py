
class Environment:
    def __init__(self):
        self.path = ["A", "C", "D", "B", "D"]

    def get_percept(self, step):
        return self.path[step]


class ModelBasedAgent:
    def __init__(self):
        self.has_key = False

    def act(self, room):
        if room == "B":
            self.has_key = True
            return "Picked up keycard"

        elif room == "D":
            if self.has_key:
                return "Access granted"
            else:
                return "Access denied"

        return f"Patrolling {room}"


def run_agent(agent, environment):
    for i in range(len(environment.path)):
        room = environment.get_percept(i)
        action = agent.act(room)
        print(room, "->", action)


agent = ModelBasedAgent()
environment = Environment()
run_agent(agent, environment)


''' 
 For a secure facility simulation, write a program for a security robot 
 that navigates a set of rooms labeled A, B, C, and D, where Room D is a 
 high-security vault that requires a keycard to enter. The robot follows a 
 strict patrol path of A -> C -> D -> B -> D and must maintain an internal 
 memory state to track whether it possesses the keycard; the robot starts 
 without the key, picks it up only when it visits Room B, and must be 
 programmed to deny access to Room D on the first attempt (before visiting B) 
 while granting access on the second attempt (after visiting B), printing 
 the outcome of each attempt.
   
'''