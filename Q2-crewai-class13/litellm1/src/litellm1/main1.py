from crewai.flow.flow import Flow, listen, start
from litellm import completion
from dotenv import load_dotenv
import os

load_dotenv()


class LiteLlmFlow(Flow):
    @start()
    def start_function(self):
        output = completion(
            model=os.getenv("MODEL"),
            messages=[{
            "role": "user",
            "content": "Speak like a pirate in a funny way"
        }])

        print(output["choices"][0]["message"]["content"])
        return output


def run_litellm_flow():
    flow = LiteLlmFlow()
    flow.start_function()