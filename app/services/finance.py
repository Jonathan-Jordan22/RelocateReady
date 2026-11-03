import math
from dataclasses import dataclass


@dataclass
class SavingsPlanInput:
    monthly_rent: int
    monthly_living_cost: int # per person, excluding rent
    household_size: int
    cushion_months: int
    deposit_months: int
    one_time_costs: int
    current_savings: int
    monthly_savings: int


@dataclass
class SavingsPlanResult:
    target_amount: int
    remaining: int
    months_to_goal: int | None # None = unreachable at current savings rate


def calculate_savings_plan(plan: SavingsPlanInput) -> SavingsPlanResult:
    monthly_expenses = plan.monthly_rent + plan.monthly_living_cost * plan.household_size

    target = (
        plan.one_time_costs
        + plan.deposit_months * plan.monthly_rent
        + plan.cushion_months * monthly_expenses
    )
    remaining = max(0, target - plan.current_savings)

    if remaining == 0:
        months_to_goal = 0
    elif plan.monthly_savings <= 0:
        months_to_goal = None
    else:
        months_to_goal = math.ceil(remaining / plan.monthly_savings)


    return SavingsPlanResult(target, remaining, months_to_goal)