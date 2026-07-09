from pydantic import BaseModel, Field


class MatchRequest(BaseModel):
    goal: str = Field(default="", max_length=1000)
    focus: list[str] = Field(default_factory=list, max_length=3)
    aiNative: int = Field(default=3, ge=1, le=5)
    workStyle: list[str] = Field(default_factory=list)
    teamValues: list[str] = Field(default_factory=list, max_length=2)
    teamSize: str = ""


class MatchResponse(BaseModel):
    techScore: int
    cultureScore: int
    overall: int
    tag: str
    message: str
