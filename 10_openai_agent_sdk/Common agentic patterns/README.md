# Common Agentic Patterns  
This repository demonstrates reusable patterns for designing AI agents, focusing on modularity, efficiency, and scalability.

---

## 1. Deterministic Flows  
Break complex tasks into sequential steps, where each step is handled by a specialized agent.  

**Example: Story Generation**  
    1. **Generate an Outline** → 2. **Write the Story** → 3. **Create the Ending**  

**Key Idea:**  
- Output of one agent becomes the input for the next.  
- Ensures controlled, predictable workflows.  

📂 **File:** [`deterministic.py`](./deterministic.py)  

---  

## 2. Handoffs and Routing  
Delegate tasks to specialized sub-agents based on conditions (e.g., language, topic).  

**Example:**  
- A frontline agent receives a request → routes it to a French/German/English specialist.  

📂 **File:** [`routing.py`](./routing.py)  

---  

## 3. Agents as Tools  
Agents can act as reusable tools instead of permanent handoffs.  

**Example:** Translation Task  
- Call a translation agent *as a tool*, retain control in the main agent.  

📂 **File:** [`agents_as_tools.py`](./agents_as_tools.py)  

---  

## 4. LLM-as-a-Judge  
Use a secondary LLM to critique and refine outputs.  

**Workflow:**  
1. **Generate** → 2. **Evaluate** → 3. **Refine** (repeat).  

📂 **File:** [`llm_as_a_judge.py`](./llm_as_a_judge.py)  

---  

## 5. Parallelization  
Run multiple agents concurrently for speed or quality.  

**Use Cases:**  
- **Latency Reduction:** Independent tasks run in parallel.  
- **Quality Control:** Generate 5 translations → pick the best.  

📂 **File:** [`parallelization.py`](./parallelization.py)  

---  

## 6. Guardrails  
Validate inputs/outputs to prevent invalid agent executions.  

| Type          | Purpose                          | Example                          |  
|---------------|----------------------------------|----------------------------------|  
| **Input Guardrails** | Block invalid requests. | Fast pre-check before main agent runs. |  
| **Output Guardrails** | Ensure responses meet criteria. | Post-processing filter. |  

📂 **Files:**  
- [`input_guardrails.py`](./input_guardrails.py)  
- [`output_guardrails.py`](./output_guardrails.py)  