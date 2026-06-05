from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = ChatGroq(model = "llama-3.1-8b-instant", temperature=0.7)

prompt = PromptTemplate(
    input_variables = ["topic"],
    template = "Suggest a catchy blog title about {topic}."
)

topic = input('Enter a topic')

formatted_prompt = prompt.format(topic=topic)

blog_title = llm.predict(formatted_prompt)

print("Generated Blog Title:", blog_title)