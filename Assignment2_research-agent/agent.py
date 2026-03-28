from langchain_groq import ChatGroq
from langchain.agents import initialize_agent, AgentType
from dotenv import load_dotenv
from tools import tools

# Load API key
load_dotenv()

# LLM (Stable Groq model)
llm = ChatGroq(
    model="llama-3.1-8b-instant",   # ✅ latest working model
    temperature=0.3,
    max_tokens=1024   # 🔥 limit output size (prevents token error)
)

# Agent (ReAct)
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    max_iterations=3,              # 🔥 prevents looping
    early_stopping_method="generate"  # 🔥 stops safely
)