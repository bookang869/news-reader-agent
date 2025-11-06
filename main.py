import dotenv

dotenv.load_dotenv()

# Crew - a collaborative group of agents
# Agent - an autonomous unit that performs tasks, makes decisions, accomplish objectives, etc... using AI
# Task - a specific assignment completed by an Agent
from crewai import Crew, Agent, Task
from crewai.project import CrewBase, agent, task, crew


# Decorator 'CrewBase' allows CrewAI-specific decorators on methods: @agent, @task, @after_kickoff
@CrewBase
class TranslatorCrew:
    # 1. Create an Agent
    # anything with @agent decorator goes to self.agents
    @agent
    def translator_agent(self):
        # 3 mandatory attributes
        # -> Role: an agent's function and expertise within the crew
        # -> Goal: an individual objective that guides the agent's decision making
        # -> Backstory: context and personality to the agent to enrich interactions
        return Agent(
            # assigns attributes according to 'translator_agent' in config/agents.yaml
            config=self.agents_config["translator_agent"]
        )

    # 2. Create a Task
    # anything with @task decorator goes to self.tasks
    @task
    def translate_task(self):
        # 2 mandatory attributes
        # -> Description: a clear, concise statement of what the task entails
        # -> Expected Output: a detailed description of what the task's completion look like
        # -> Agent (OPTIONAL): the agent responsible for executing the task
        return Task(config=self.tasks_config["translate_task"])

    # 3. Create a Crew
    @crew
    def assemble_crew(self):
        # Crew is a combination of agents and tasks
        # verbose - print out agent's response
        return Crew(agents=self.agents, tasks=self.tasks, verbose=True)


TranslatorCrew().assemble_crew().kickoff(
    inputs={"sentence": "I'm Kyle and I like to ride my bicycle in Napoli"}
)
