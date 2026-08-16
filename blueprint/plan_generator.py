from .llm import structured
from .prompts import PLAN_GENERATOR_PROMPT
from .schemas import Plan, Step, UserProfile

def generate(profile: UserProfile) -> Plan:
    result = structured(Plan, PLAN_GENERATOR_PROMPT.format(profile=profile.model_dump_json(), similar_journeys="Bundled journey references"))
    if result: return result
    names = [("Define the buyer", "research"), ("Interview 10 target users", "interview"), ("Map the painful workflow", "research"), ("Run a 48-hour test", "validate"), ("Price a paid pilot", "sell"), ("Deliver the smallest version", "build"), ("Review evidence and costs", "measure"), ("Choose the next commitment", "operate")]
    steps = [Step(number=i, name=n, what_to_do=f"Complete {n.lower()} for {profile.idea}.", why_it_matters="This turns an assumption into evidence before the next commitment.", resources=["A simple spreadsheet", "Ten direct conversations"], done_criteria="Write down evidence, decision, and next action.", estimated_time_days=2 + i, estimated_cost_dollars=25 * (i % 3), estimated_hours=3 + i, step_type=t) for i,(n,t) in enumerate(names, 1)]
    return Plan(steps=steps, total_estimated_days=sum(s.estimated_time_days for s in steps), goal_reached_description=f"A tested first version of {profile.idea} with a decision grounded in customer evidence.")

