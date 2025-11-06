import dotenv

dotenv.load_dotenv()

# Crew - a collaborative group of agents
# Agent - an autonomous unit that performs tasks, makes decisions, accomplish objectives, etc... using AI
# Task - a specific assignment completed by an Agent
from crewai import Crew, Agent, Task
from crewai.project import CrewBase, agent, task


# Decorator 'CrewBase' allows CrewAI-specific decorators on methods: @agent, @task, @after_kickoff
@CrewBase
class TranslatorCrew:
    # 1. Create an Agent
    @agent
    def translator_agent(self):
        # 3 mandatory attributes
        # -> Role: agent's function and expertise within the crew
        # -> Goal: individual objective that guides the agent's decision making
        # -> Backstory: context and personality to the agent to enrich interactions
        return Agent(
            role="Translator to translate from English to Italian",
            goal="To be a good and useful translator to avoid misunderstandings.",
            backstory="You grew up between New York and Palermo, you can speak both English and Italian fluently, and you can detect cultural differences.",
        )
