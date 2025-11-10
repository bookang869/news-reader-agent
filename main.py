# load environment variables from .env
import dotenv

dotenv.load_dotenv()

# Crew - a collaborative group of agents
# Agent - an autonomous unit that performs tasks, makes decisions, accomplish objectives, etc... using AI
# Task - a specific assignment completed by an Agent

from crewai import Crew, Agent, Task
from crewai.project import CrewBase, agent, task, crew
from tools import search_tool, scrape_tool


@CrewBase
class NewsReaderAgent:
    # 1. Create agents

    @agent
    # The agent that discovers and collects most relevant, credible, up-to-date news articles
    def news_hunter_agent(self):
        return Agent(
            config=self.agents_config["news_hunter_agent"],
            tools=[search_tool, scrape_tool],
        )

    # The agent that transforms raw articles to cleaer, concise, and comprehensive summaries
    @agent
    def summarizer_agent(self):
        return Agent(config=self.agents_config["summarizer_agent"], tools=[scrape_tool])

    # The agent that curates news content into a cohesive, engaging narrative
    @agent
    def curator_agent(self):
        return Agent(config=self.agents_config["curator_agent"])

    # 2. Create tasks for the above agents

    @task
    # The task for the 'news_hunter_agent'
    def content_harvesting_task(self):
        return Task(config=self.tasks_config["content_harvesting_task"])

    # The task for the 'summarizer_agent'
    @task
    def summarization_task(self):
        return Task(config=self.tasks_config["summarization_task"])

    # The task for the 'curator_agent'
    @task
    def final_report_assembly_task(self):
        return Task(config=self.tasks_config["final_report_assembly_task"])

    # 3. Create a crew combining these agents and tasks

    @crew
    def crew(self):
        return Crew(agents=self.agents, tasks=self.tasks, verbose=True)


# execute the crew
NewsReaderAgent().crew().kickoff(inputs={"topic": "Cambodia Thailand War."})
