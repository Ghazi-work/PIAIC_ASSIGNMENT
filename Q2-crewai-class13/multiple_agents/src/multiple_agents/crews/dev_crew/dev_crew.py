from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai import LLM


## We will give different LLM to each agent
llm1 = LLM(model="ollama/llama3.2:latest", base_url="http://127.0.0.1:11434")   ## Local LLM model
llm2 = LLM(model="gemini/gemini-1.5-flash")


@CrewBase
class DevCrew:
    """Dev Crew"""

   
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

  
    @agent
    def junior_python_developer(self) -> Agent:
        return Agent(
            config=self.agents_config["junior_python_developer"],
            llm=llm1
        )

    @agent
    def senior_python_developer(self) -> Agent:
        return Agent(
            config=self.agents_config["senior_python_developer"],
            llm=llm2
        )


    @task
    def write_python_code(self) -> Task:
        return Task(
            config=self.tasks_config["write_python_code"],
        )

    @task
    def review_python_code(self) -> Task:
        return Task(
            config=self.tasks_config["review_python_code"],
        )
    
    @crew
    def crew(self) -> Crew:
        """Creates the Developer Crew"""
        

        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
