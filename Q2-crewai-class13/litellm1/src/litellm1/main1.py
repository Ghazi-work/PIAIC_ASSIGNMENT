from crewai.flow.flow import Flow, listen, start
from litellm import completion
from dotenv import load_dotenv
import os

load_dotenv()


## In the env

## TO call a remote model use the following
# GEMINI_API_KEY=AIzaSyC5ZvCIdp3EdCWEy03oHZCS4_DAw5GnZcI
# MODEL=gemini/gemini-1.5-flash

## TO call a local model use the following
#MODEL=ollama/llama3.2:latest
#BASE_URL=http://127.0.0.1:11434

class LiteLlmFlow(Flow):
    @start()
    def start_function(self):
        output = completion(
            model=os.getenv("MODEL"),
            messages=[{
            "role": "user",
            "content": "Write a motivational poem on my name which is Ghazi"
        }])

        print(output["choices"][0]["message"]["content"])
        return output


def run_litellm_flow():
    flow = LiteLlmFlow()
    flow.start_function()