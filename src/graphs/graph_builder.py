from langgraph.graph import StateGraph, START, END
from src.llms.groqllm import GroqLLM
from src.states.blogstate import BlogState
from src.nodes.blog_nodes import BlogNode

class GraphBuilder:
    def __init__(self,llm):
        self.llm=llm
        self.graph=StateGraph(BlogState)

    def build_topic_graph(self):
        """
        Build a graph to generate blogss based on topic
        """
        self.blog_node_obj=BlogNode(self.llm)
        print(self.llm)
        ## Nodes
        self.graph.add_node("title_creation", self.blog_node_obj.title_creation)
        self.graph.add_node("content_generation",self.blog_node_obj.content_generation)

        ## Edges
        self.graph.add_edge(START,"title_creation")
        self.graph.add_edge("title_creation","content_generation")
        self.graph.add_edge("content_generation",END)

        return self.graph
    
    def build_language_graph(self):
        """
        Build a graph for blog generation with inputs topic and language
        """
        self.blog_node_obj=BlogNode(self.llm)
        print(self.llm)
        ## Nodes
        self.graph.add_node("title_creation", self.blog_node_obj.title_creation)
        self.graph.add_node("content_generation", self.blog_node_obj.content_generation)

        self.graph.add_node("hindi_translation", lambda state: self.blog_node_obj.translation({**state, "current_language": "hindi"}))
        self.graph.add_node("french_translation", lambda state: self.blog_node_obj.translation({**state, "current_language": "french"}))
        self.graph.add_node("spanish_translation", lambda state: self.blog_node_obj.translation({**state, "current_language": "spanish"}))
        self.graph.add_node("portuguese_translation", lambda state: self.blog_node_obj.translation({**state, "current_language": "portuguese"}))
        self.graph.add_node("chinese_translation", lambda state: self.blog_node_obj.translation({**state, "current_language": "chinese"}))
        self.graph.add_node("japanese_translation", lambda state: self.blog_node_obj.translation({**state, "current_language": "japanese"}))
        self.graph.add_node("russian_translation", lambda state: self.blog_node_obj.translation({**state, "current_language": "russian"}))

        self.graph.add_node("route", self.blog_node_obj.route)


        ## edges and conditional edges
        self.graph.add_edge(START, "title_creation")
        self.graph.add_edge("title_creation", "content_generation")
        self.graph.add_edge("content_generation", "route")

        ## conditional edge
        self.graph.add_conditional_edges(
            "route",
            self.blog_node_obj.route_decision,
            {
                "hindi":"hindi_translation",
                "french":"french_translation",
                "spanish": "spanish_translation",
                "portuguese": "portuguese_translation",
                "chinese": "chinese_translation",
                "japanese": "japanese_translation",
                "russian": "russian_translation"
            }
        )
        self.graph.add_edge("hindi_translation", END)
        self.graph.add_edge("french_translation", END)
        self.graph.add_edge("spanish_translation", END)
        self.graph.add_edge("portuguese_translation", END)
        self.graph.add_edge("chinese_translation", END)
        self.graph.add_edge("japanese_translation", END)
        self.graph.add_edge("russian_translation", END)
        return self.graph

    
    def setup_graph(self,usecase):
        if usecase=="topic":
            self.build_topic_graph()
        if usecase=="language":
            print("Language block")
            self.build_language_graph()

        return self.graph.compile()

## Below code is for the langsmith langgraph studio
llm=GroqLLM().get_llm()

## get the graph
graph_builder=GraphBuilder(llm)
# we will pss this graph variable into our langgraph.json file in order to visualize and debug it in langgraph studio
graph=graph_builder.build_language_graph().compile() 

