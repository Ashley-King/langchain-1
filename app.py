from langchain.llms import OpenAI
import dotenv
import os
dotenv.load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY")
llm = OpenAI(openai_api_key=openai_key)

print(llm("Here is a fun fact about Pluto:"))