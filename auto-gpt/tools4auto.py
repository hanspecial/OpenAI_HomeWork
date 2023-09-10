from langchain.utilities import SerpAPIWrapper
from langchain.agents import Tool
from langchain.tools.file_management.write import WriteFileTool
from langchain.tools.file_management.read import ReadFileTool

import os
os.environ["SERPAPI_API_KEY"] = "e65622355785aba531fe0f3733c6c429e3ec43457c916a0c3006e6f81d433369"

class Tools4Auto:
    def __init__(self):
        search = SerpAPIWrapper()
        self.tools = [
            Tool(
                name="search",
                func=search.run,
                description="useful for when you need to answer questions about current events. You should ask targeted questions",
            ),
            WriteFileTool(),
            ReadFileTool(),
        ]