# Import the Uvicorn server to run the FastAPI application
import uvicorn

# Import FastAPI and Request object to handle incoming HTTP requests
from fastapi import FastAPI, Request

# Import your custom GraphBuilder and GroqLLM components
from src.graphs.graph_builder import GraphBuilder
from src.llms.groqllm import GroqLLM

# Standard Python modules
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Initialize the FastAPI app
app = FastAPI()

# Debug print to ensure the LANGCHAIN_API_KEY is loaded properly
print(os.getenv("LANGCHAIN_API_KEY"))

# Set LANGSMITH_API_KEY in the environment using the LANGCHAIN_API_KEY
os.environ["LANGSMITH_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

# ----------------------------
# Define API route to handle blog generation
# ----------------------------

@app.post("/blogs")
async def create_blogs(request: Request):
    """
    Endpoint to generate blog content using topic and optional language.
    Accepts POST requests with JSON body.
    """

    # Parse JSON data from the request body
    data = await request.json()
    
    # Extract 'topic' and 'language' from the request (default to empty string if missing)
    topic = data.get("topic", "")
    language = data.get("language", "")
    print(language)  # Debug print to verify incoming language

    # Initialize the custom LLM (Groq-provided model wrapper)
    groqllm = GroqLLM()
    llm = groqllm.get_llm()

    # Initialize the graph builder with the LLM
    graph_builder = GraphBuilder(llm)

    # Handle case where both topic and language are provided
    if topic and language:
        # Set up graph logic based on language-specific use case
        graph = graph_builder.setup_graph(usecase="language")
        # Invoke the graph with both topic and language
        state = graph.invoke({"topic": topic, "current_language": language.lower()})

    # Handle case where only topic is provided
    elif topic:
        # Set up graph logic for topic-only use case
        graph = graph_builder.setup_graph(usecase="topic")
        # Invoke the graph with topic only
        state = graph.invoke({"topic": topic})

    # Return the result as a JSON response
    return {"data": state}

# ----------------------------
# Run the app with Uvicorn if this script is executed directly
# ----------------------------
if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
