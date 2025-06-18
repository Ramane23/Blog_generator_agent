# 🧠 Blog Generator Agent

**Blog Generator Agent** is a modular, agentic AI application designed to automatically generate and translate blogs using LLMs. It leverages **HLangChain**, **LangGraph**, and **Groq-backed LLaMA 3**, and is served as a high-performance API via **FastAPI**. Monitoring and tracing are powered by **LangSmith**.

---

## ⚙️ Tech Stack

| Layer           | Technology              |
|----------------|--------------------------|
| Orchestration   | `HLangChain`, `LangGraph` |
| LLM Backend     | `Groq` (e.g., LLaMA 3)    |
| API Framework   | `FastAPI`                |
| Monitoring      | `LangSmith`              |
| Workspace Mgmt  | `uv`                     |
| Tools           | Arxiv, Translators, etc. |

---

## 📌 Features

- ✅ Title generation  
- ✅ Blog content creation  
- ✅ Multilingual translation:
  - French
  - Spanish
  - Japanese
  - Chinese
  - Russian
  - Portuguese
  - Hindi  
- ✅ Fast, traceable API using Groq + LangSmith  
- ✅ Easy extensibility with LangGraph nodes

---

## 🧠 Agent Graph (LangGraph)

![Agent Graph](https://githubimagesbucket.s3.us-east-1.amazonaws.com/blog_generator_agents.PNG)

> The left graph represents the **full multilingual version** with routing and translation branches. The right graph shows a **minimal core version** without translation nodes.

---

## 🛠️ Setup

### 📥 Clone the repository

```bash
git clone https://github.com/your-username/blog_generator_agent.git
cd blog_generator_agent
```

### 📦 Create and activate the virtual environment using `uv`

```bash
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt
```

### 🔧 Environment Variables

Create a `.env` file in the root:

```env
GROQ_API_KEY=your-groq-key
LANGSMITH_API_KEY=your-langsmith-key
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=blog-generator-agent
```

---

## 🚀 Running the Project

### 🔹 Start the FastAPI server

```bash
python app.py
```

### 🔹 Launch LangGraph Studio (for interactive development & debugging)

```bash
langgraph dev
```

LangGraph Studio provides a visual interface for testing and inspecting the agent pipeline.

---

## 📊 Monitoring with LangSmith

LangSmith is integrated for:

- Real-time tracing of agent steps
- Tool usage analysis
- Debugging and insight into agent behavior

You can view traces in your LangSmith dashboard under the `blog-generator-agent` project.

---

## 🧪 Example Usage (API Call)

**Endpoint:** `/generate`

**POST Body:**
```json
{
  "topic": "The impact of AI on education",
  "language": "japanese"
}
```

This request will generate a blog post on the specified topic and return the translation in the selected language only.

> Supported values for `language`:  
> `"french"`, `"spanish"`, `"japanese"`, `"chinese"`, `"russian"`, `"portuguese"`, `"hindi"`, or `"all"` to receive translations in every supported language.

---

