class Environment:
    def __init__(self):
        # 9 planting beds
        self.beds = [
            "Moist", "Dry", "Moist",
            "Moist", "Dry", "Moist",
            "Dry", "Moist", "Moist"
        ]

    def get_percept(self, position):
        return self.beds[position]

    def water_bed(self, position):
        self.beds[position] = "Moist"


class SimpleReflexAgent:
    def act(self, percept):
        if percept == "Dry":
            return "Watering bed"
        return "Already moist"


def run_agent(agent, environment):
    for i in range(9):
        percept = environment.get_percept(i)
        action = agent.act(percept)

        print(f"Bed {i+1}: {percept} -> {action}")

        if percept == "Dry":
            environment.water_bed(i)

    print("Final Beds:", environment.beds)


agent = SimpleReflexAgent()
environment = Environment()
run_agent(agent, environment)


''' 
 In a high-tech greenhouse, you need to implement an automated irrigation robot
   that operates on a simple reflex logic to maintain soil moisture. 
   The greenhouse consists of 9 planting beds, represented by a list where 
   beds 2, 5, and 7 are initially detected as "Dry" and all others as "Moist." 
   The robot must traverse the beds sequentially from 1 to 9, checking the state 
   of each bed; if a bed is "Dry," the robot should water it, change its status
   to "Moist," and print a confirmation message, but if the bed is already "Moist,"
   it should simply move to the next one, displaying the final status of all beds
   after the process is complete.
   
'''