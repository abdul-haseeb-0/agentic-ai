# 🛠️ LLM & Prompt Engineering Guide 🌐

Master the art of **Large Language Models (LLMs)** and **Prompt Engineering**! 🚀

---

## 🔑 Key Settings

| Setting            | Purpose                              |
|--------------------|--------------------------------------|
| **temperature**    | Controls creativity: Low = Focused, High = Creative |
| **top_p**          | Picks from a pool covering top probability mass |
| **max_tokens**     | Maximum length of the generated output |
| **frequency_penalty** | Reduces repetition in output       |
| **presence_penalty** | Encourages introducing new topics   |

---

## 📚 Example Code

```python
from langchain_google_genai import GoogleGenerativeAI

llm = GoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.7,
    top_p=0.9,
    max_tokens=500
)
```

---

Explore the power of LLMs and elevate your AI projects! 🌟

Connect with me on [LinkedIn](https://www.linkedin.com/in/abdul-haseeb-980075323/) for more updates.
