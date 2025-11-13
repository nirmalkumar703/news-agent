from crewai import Task
from agent import news_reporter_agent,news_reviewer_agent,news_creater_agent

reporter_task=Task(
    description=("Create a detailed and accurate news report based on the {query}."
                 "you can utilise serper dev tool to get the latest information about the news"
                "Make sure to maintain all important information and provide proper citations where necessary."),
    expected_output="A comprehensive news report in text farmate.",
    agent=news_reporter_agent,
    verbose=True
)

reviewer_task=Task(
    description=("review the news reported created by news reporter accurate news report."
                 "you can utilise serper dev tool to get the information about the news and scrape website tool to scrap news from websiter to cross verify the information from multiple sources."
                "Make sure to fact-check all information provided by the news reporter and provide suggestions for improvement if necessary."),
    expected_output="A comprehensive news report in markdown formate, separated by news name with time.",
    agent=news_reviewer_agent,
    verbose=True
)
creater_task=Task(
    description=("create news by using the markdoen report, created by news reviewer ."
                 "you can utilise serper dev tool to get the information about the news and scrape website tool to scrap news from websiter to cross verify the information from multiple sources."
                "Make sure to engaging and reader-friendly."
                "you can use suggestions given by news revieweer for improvement if necessary."),
    expected_output="A comprehensive news in markdown formate, separated by news name with time.",
    agent=news_creater_agent,
    verbose=True
)

