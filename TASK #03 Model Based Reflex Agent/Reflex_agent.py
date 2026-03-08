class Environment:
    def __init__(self, temperature):
        self.temperature = temperature

    def get_temperature(self):
        return self.temperature

    def set_temperature(self, temperature):
        self.temperature = temperature


class ModelBasedReflexAgent:
    def __init__(self, threshold_low=18, threshold_high=25):
        self.threshold_low = threshold_low
        self.threshold_high = threshold_high
        self.previous_action = None  # Internal model (memory)
        self.heater_on = False

    def perceive(self, environment):
        return environment.get_temperature()

    def update_model(self, action):
        self.previous_action = action

    def decide_action(self, temperature):
        if temperature < self.threshold_low:
            if self.previous_action == "TURN_ON_HEATER":
                action = "HEATER_ALREADY_ON"
            else:
                action = "TURN_ON_HEATER"
                self.heater_on = True

        elif temperature > self.threshold_high:
            if self.previous_action == "TURN_OFF_HEATER":
                action = "HEATER_ALREADY_OFF"
            else:
                action = "TURN_OFF_HEATER"
                self.heater_on = False

        else:
            action = "NO_ACTION_NEEDED"

        return action

    def run(self, environment):
        temperature = self.perceive(environment)
        print(f"Current Temperature : {temperature}°C")
        print(f"Previous Action     : {self.previous_action}")

        action = self.decide_action(temperature)
        self.update_model(action)

        print(f"Action Taken        : {action}")
        print(f"Heater Status       : {'ON' if self.heater_on else 'OFF'}")

if __name__ == "__main__":
    env = Environment(temperature=15)
    agent = ModelBasedReflexAgent(threshold_low=18, threshold_high=25)

 
    print("   Model-Based Reflex Agent Simulation")


    print("\nScenario 1: Temperature = 15°C (Cold)")
    env.set_temperature(15)
    agent.run(env)

    print("Scenario 2: Temperature = 15°C (Cold again)")
    env.set_temperature(15)
    agent.run(env)

    print("Scenario 3: Temperature = 22°C (Comfortable)")
    env.set_temperature(22)
    agent.run(env)

    print("Scenario 4: Temperature = 30°C (Hot)")
    env.set_temperature(30)
    agent.run(env)

    print("Scenario 5: Temperature = 30°C (Hot again)")
    env.set_temperature(30)
    agent.run(env)
