import streamlit as st
from src.langgraph_agents.ui.streamlit.loadui import LoadStreamlitUI
from src.langgraph_agents.models.groqllm import GroqLLM
from src.langgraph_agents.graph.graph_builder import GraphBuilder
from src.langgraph_agents.ui.streamlit.display_result import DisplayResultsStreamlit


def load_langgraph_agentical_app():
    """
    Loads and runs the LangGraph AgenticAI application with Streamlit UI. 
    This function initializes the UI, handles user input, configure the LLM model,
    sets up the graph based on the selected use case, and displays the output while
    implementing exception handling for robustness
    
    """

    ## Load UI
    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()

    if not user_input:
        st.error("Error: Failed to load user input from the UI")
        return
    
    user_message = st.chat_input("Ask something...")

    if user_message:
        try:
            ## Configure the LLM's 
            obj_llm_config = GroqLLM(user_controls_input=user_input)
            model = obj_llm_config.get_llm_models()

            if not model:
                st.error("Error: LLM model could not be initialized")
                return 
            
            # Initialize and setup graph based on usecase
            usecase = user_input.get("selected_usecase")
            if not usecase:
                st.error("Error: Usecase not selected")
                return 

            graph_builder = GraphBuilder(model)
            try:
                graph = graph_builder.setup_graph(usecase)
                display = DisplayResultsStreamlit(usecase, graph, user_message)
                display.display_result_on_ui()
            except Exception as e:
                st.error(f"Error: Graph setup failed - {e}")
                return

        
        except Exception as e:
            return e

    
