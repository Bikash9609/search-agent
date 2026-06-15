from typing import List
from pydantic import BaseModel, Field


class Source(BaseModel):
    """Schema for source used by the agent"""

    url: str = Field(description="The url of the source")


class AgentResponse(BaseModel):
    """Schema for the agent response with answer and sources"""

    answer: str = Field(description="Final answer in markdown format for the query")
    sources: List[Source] = Field(
        default_factory=List, description="List of sources used to generate the answer"
    )
