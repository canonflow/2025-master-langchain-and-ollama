import os
from dotenv import load_dotenv
from langchain_ollama import ChatOllama

from langchain_core.prompts import (
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    ChatPromptTemplate
)
from langchain_core.output_parsers import StrOutputParser

load_dotenv("./../../.env")

BASE_URL = os.getenv('OLLAMA_BASE_URL')
MODEL = "llama3.2:latest"

LLM = ChatOllama(
    base_url=BASE_URL,
    model=MODEL,
)

system_template = SystemMessagePromptTemplate.from_template(
    """
    You are helpful AI assistant who answer question based on the provided context.
    """
)

prompt = """Answer user question based on the provided context ONLY! If do not know the answer or the question is not 
relevant with the context, just say "I don't know".

### Context:
{context}

### Question:
{question}

### Answer:
"""

human_template = HumanMessagePromptTemplate.from_template(prompt)

messages = [system_template, human_template]
template = ChatPromptTemplate(messages=messages)

chain = template | LLM | StrOutputParser()


def ask_llm(context, question):
    return chain.invoke({
        "context": context,
        "question": question,
    })
