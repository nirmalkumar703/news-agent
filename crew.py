from crewai import Crew,Process
from agent import news_reporter_agent,news_reviewer_agent,news_creater_agent
from task import reporter_task,reviewer_task,creater_task

news_crew=Crew(
    tasks=[
        reporter_task,
        reviewer_task,
        creater_task
    ],
    agents=[
        news_reporter_agent,
        news_reviewer_agent,
        news_creater_agent
    ],
    process=Process.sequential
)