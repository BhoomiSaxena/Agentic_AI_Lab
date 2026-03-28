from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.tools.wikipedia.tool import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper

search = DuckDuckGoSearchRun()

wiki = WikipediaQueryRun(
    api_wrapper=WikipediaAPIWrapper()
)

tools = [search, wiki]