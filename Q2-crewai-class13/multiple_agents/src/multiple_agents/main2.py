from crewai.flow import Flow, listen, start

from multiple_agents.crews.dev_crew.dev_crew import DevCrew 

class DevFlow(Flow):

    @start()
    def problem_input(self):
        output = DevCrew().crew().kickoff(
            inputs = {
            "problem": "Write a Python code that takes number list and returns even numbers"
        }
        )
        return output.raw


def run_dev_flow():
    dev_flow = DevFlow()
    result = dev_flow.kickoff()
    print(result)