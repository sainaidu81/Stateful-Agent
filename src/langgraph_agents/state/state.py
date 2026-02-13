from typing import Annotated
from typing_extensions import TypedDict, List
from langgraph.graph.message import add_messages
from pydantic import BaseModel, Field

class State(TypedDict):
    """
    Represent the structure of the state used in graph
    
    """

    messages : Annotated[List, add_messages]