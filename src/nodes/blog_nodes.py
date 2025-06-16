from src.states.blogstate import BlogState

# Define a class to represent a blog generation node/agent
class BlogNode:
    """
    A class to represent the blog node.
    This node uses an LLM to generate blog titles and content.
    """

    # Constructor to initialize the LLM instance used by this node
    def __init__(self, llm):
        # Store the language model instance as an attribute
        self.llm = llm

    # Method to generate a blog title based on a given state
    def title_creation(self, state: BlogState):
        """
        Create the title for the blog using the topic provided in the state.
        """

        # Check if the topic exists and is not empty in the state
        if "topic" in state and state["topic"]:
            # Define a prompt template for generating a blog title
            prompt = """
                   You are an expert blog content writer. Use Markdown formatting. Generate
                   a blog title for the {topic}. This title should be creative and SEO friendly
                   """

            # Format the prompt with the provided topic
            sytem_message = prompt.format(topic=state["topic"])
            print(sytem_message)  # (Optional) Debug: print the final prompt

            # Call the LLM with the system message prompt
            response = self.llm.invoke(sytem_message)
            print(response)  # (Optional) Debug: print the LLM's response

            # Return a new state dictionary with the generated title
            return {"blog": {"title": response.content}}

    # Method to generate blog content using the topic and title in the state
    def content_generation(self, state: BlogState):
        # Check that a topic is provided in the state
        if "topic" in state and state["topic"]:
            # Create a prompt for detailed blog content generation
            system_prompt = """You are expert blog writer. Use Markdown formatting.
            Generate a detailed blog content with detailed breakdown for the {topic}"""

            # Format the prompt with the current topic
            system_message = system_prompt.format(topic=state["topic"])

            # Use the LLM to generate blog content
            response = self.llm.invoke(system_message)

            # Return a new state with both title and generated content
            return {"blog": {"title": state['blog']['title'], "content": response.content}}
