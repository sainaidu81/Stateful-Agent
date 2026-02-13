import streamlit as st
import os 

from src.langgraph_agents.ui.ui_configfile import Config

class LoadStreamlitUI:
    def __init__(self):
        self.config=Config()
        self.user_controls = {}
    
    def load_streamlit_ui(self):
        st.set_page_config(page_title=""+ self.config.page_title(), layout="wide")
        st.header(""+self.config.page_title())

        with st.sidebar:
            # Get options
            llm_options = self.config.get_llm_options()
            usecase_options = self.config.usecase_options()

            # LLM selection
            self.user_controls["selected_llm"] = st.selectbox("Select LLM", llm_options)

            if self.user_controls["selected_llm"] == "Groq":
                model_options = self.config.get_groq_models()
                self.user_controls["selected_groq_model"] = st.selectbox("Select Model", model_options)
                self.user_controls["GROQ_API_KEY"]= st.session_state["GROQ_API_KEY"]=st.text_input("API Key", type="password")
                
                if not self.user_controls["GROQ_API_KEY"]:
                    st.warning("Please enter the API key to continue, Don't have? refer: https://console.groq.com/keys")
            
            # usecase selection
            self.user_controls["selected_usecase"] = st.selectbox("Select Chat Mode", usecase_options)
    
        return self.user_controls