from langgraph.graph import StateGraph, START, END
from typing import TypedDict

# Define state
class BMISTATE(TypedDict):
    weight: float
    height: float
    bmi: float

def calculate_bmi(state: BMISTATE) -> BMISTATE:
    # Use bracket notation to access dictionary values
    state['bmi'] = state['weight'] / (state['height'] ** 2)
    return state

# Define graph
graph = StateGraph(BMISTATE)

graph.add_node("calculate_bmi", calculate_bmi)

graph.add_edge(START, "calculate_bmi")
graph.add_edge("calculate_bmi", END)

workflow = graph.compile()

# Fix the typo: intial_state -> initial_state
initial_state = {"weight": 70, "height": 1.75}

# Run the workflow
final_state = workflow.invoke(initial_state)
print(f"Final state: {final_state}")
print(f"BMI: {final_state['bmi']:.2f}") 