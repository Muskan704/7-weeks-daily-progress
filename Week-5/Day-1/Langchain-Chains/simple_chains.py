from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt = PromptTemplate(
    template = 'Generate5 interesting facts about {topics}',
    input_variables = ['topic']
)

model = ChatGroq(model="llama-3.1-8b-instant")

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({'topics':'cricket'})

print(result)

chain.get_graph().print_ascii()
