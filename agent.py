from crewai import Agent

from crewai_tools import SerperDevTool,ScrapeWebsiteTool

import os
from dotenv import load_dotenv
load_dotenv()

key = os.getenv("OPENAI_API_KEY")
if key:
    print("✅ OPENAI_API_KEY loaded:", key[:8], "...")
else:
    print("❌ Key not found! Check .env file location or spelling.")


serper_tool=SerperDevTool()
scraptool=ScrapeWebsiteTool()

news_reporter_agent = Agent(
    name="News Reporter Agent",
    role="You are a news reporter agent that creates detailed and accurate news reports based on {query}",
    goal="your report is must be related to curent news amd must be accurate",
    backstory="You have 20 years of experience in journalism and reporting and working in bbc for past 10 years",
    tools=[serper_tool,scraptool],
    llm="gpt-4.1-mini")


news_reviewer_agent = Agent(
    name="news reviewer",
    role="you are a news reviewer, review the news for it's accuracy and Authenticity",
    goal="your review must accurate and curect without any error",
    backstory=("you have 20 years experience in reviewing the news report give my news reporter"
                "you have secure 7 award for being best news reviewer in ypur company"
                "you have worked with bbc for past 10 years as a senior news reviewer"
            ),
    tools=[serper_tool,scraptool],
    llm="gpt-4.1-mini")

news_creater_agent = Agent(
    name="News Creater Agent",
    role="You are a news creater agent that you craft news",
    goal="your news creater, your news must be detailedmand engaging",
    backstory="You have 20 years of experience in journalism and reporting and working in bbc for past 10 years",
    tools=[serper_tool,scraptool],
    llm="gpt-4.1-mini")
    