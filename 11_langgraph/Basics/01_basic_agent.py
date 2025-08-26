from langgraph.graph import StateGraph, START, END
from typing_extensions import TypedDict
import random

# # Define the state type for the graph
class state(TypedDict):
    prompt: str

# # Define the agents
def agent_a(state):
    print("---Agent A---", state['prompt'])
    return {"prompt": state['prompt'] + " I am"}

def agent_b(state):
    print("---Agent B---", state['prompt'])
    return {"prompt": state['prompt'] + " happy!"}

def agent_c(state):
    print("---Agent C---", state['prompt'])
    return {"prompt": state['prompt'] + " sad!"}

# # Define the condition for choosing the next agent
def condition(state: state):
    return random.choice(["Agent B", "Agent C"])

# Create the state graph and add nodes and edges
builder = StateGraph(state)

builder.add_node("Agent A", agent_a)
builder.add_node("Agent B", agent_b)
builder.add_node("Agent C", agent_c)

builder.add_edges(START, "Agent A")
builder.add_conditional_edges("Agent A", condition)
builder.add_edges("Agent B", END)
builder.add_edges("Agent C", END)

# Compile the graph
graph = builder.compile()

# Invoke the graph with an initial state
output = graph.invoke({
    "prompt": "Hi, this is Haseeb"
})

print("Final Output:", output)
