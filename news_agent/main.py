from crew import news_crew

import os
from dotenv import load_dotenv
load_dotenv()

key = os.getenv("OPENAI_API_KEY")
if key:
    print("✅ OPENAI_API_KEY loaded:", key[:8], "...")
else:
    print("❌ Key not found! Check .env file location or spelling.")


if __name__=="__main__":
    query="coimbatore girl gang rape case"
    result=news_crew.kickoff(inputs={"query":query})
    print(result)
