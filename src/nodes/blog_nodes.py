from src.states.blogstate import BlogState
from src.states.blogstate import Blog
from langchain_core.messages import SystemMessage, HumanMessage

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

    def translation(self,state:BlogState):
        """
        Translate the content to the specified language.
        """
        translation_prompt="""
        Translate the following content into {current_language}.
        - Maintain the original tone, style, and formatting.
        - Adapt cultural references and idioms to be appropriate for {current_language}.

        ORIGINAL CONTENT:
        {blog_content}

        """
        print(state["current_language"])
        blog_content=state["blog"]["content"]
        messages=[
            HumanMessage(translation_prompt.format(current_language=state["current_language"], blog_content=blog_content))

        ]
        transaltion_content = self.llm.with_structured_output(Blog).invoke(messages)
        return {"blog": {"content": transaltion_content}}

    def route(self, state: BlogState):
        return {"current_language": state['current_language'] }
    

    def route_decision(self, state: BlogState):
        """
        Route the content to the respective translation function.
        """
        if state["current_language"] == "spanish":
            return "spanish"
        elif state["current_language"] == "french": 
            return "french"
        elif state["current_language"] == "chinese": 
            return "chinese"
        elif state["current_language"] == "russian": 
            return "russian"
        elif state["current_language"] == "japanese": 
            return "japanese"
        elif state["current_language"] == "corean": 
            return "corean"
        elif state["current_language"] == "portugese": 
            return "portugese"
        elif state["current_language"] == "hindi": 
            return "hindi"
        else:
            return state['current_language']