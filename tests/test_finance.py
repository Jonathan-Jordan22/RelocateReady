from app.services.finance import SavingsPlanInput, calculate_savings_plan

def make_input(**overrides):
    values = dict(
        monthly_rent=1500,
        monthly_living_cost=1000,
        household_size=2,
        cushion_months=3,
        deposit_months=2,
        one_time_costs=5000,
        current_savings=4000,
        monthly_savings=1000,
    )
    values.update(overrides)
    return SavingsPlanInput(**values)

def test_target_includes_one_time_costs_deposit_and_cushion():
    result = calculate_savings_plan(make_input())
    assert result.target_amount == 18500
    assert result.remaining == 14500

def test_months_to_goal_rounds_up_partial_months():
    result = calculate_savings_plan(make_input())
    assert result.months_to_goal == 15

def test_already_saved_enough():
    result = calculate_savings_plan(make_input(current_savings=20000))
    assert result.remaining == 0
    assert result.months_to_goal == 0

def test_no_monthly_saving_means_goal_is_unreachable():
    result = calculate_savings_plan(make_input(monthly_savings=0))
    assert result.months_to_goal is None