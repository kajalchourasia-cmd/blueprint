from typing import Literal
from pydantic import BaseModel, Field

IdeaType = Literal["physical_business", "retail_store", "service", "saas", "ai_product", "marketplace", "creator", "consumer_product", "other"]
Goal = Literal["get_job", "side_income", "small_business", "startup", "raise_money", "just_explore"]

class UserProfile(BaseModel):
    idea: str
    idea_type: IdeaType
    location: str
    background: str
    life_context: list[str]
    goal: Goal
    hours_per_week: int
    money_available: int

class RealityCheck(BaseModel):
    fit_score: int = Field(ge=1, le=10)
    fit_rationale: str
    unfair_advantages: list[str] = Field(min_length=3, max_length=3)
    critical_gaps: list[str] = Field(min_length=3, max_length=3)
    specific_delusions: list[dict]

class Step(BaseModel):
    number: int
    name: str
    what_to_do: str
    why_it_matters: str
    resources: list[str]
    done_criteria: str
    estimated_time_days: int
    estimated_cost_dollars: int
    estimated_hours: int
    step_type: str

class Plan(BaseModel):
    steps: list[Step] = Field(min_length=8, max_length=15)
    total_estimated_days: int
    goal_reached_description: str

class GapLayer(BaseModel):
    layer_type: Literal["unseen", "missing_voice", "real_cost"]
    content: str
    ledger_delta: dict | None = None

class CostLedger(BaseModel):
    cash_dollars: int
    hours_invested: int
    relationship_impact_days: int
    health_impact_score: int
    opportunity_cost_dollars: int
    projected_3yr_total: int

