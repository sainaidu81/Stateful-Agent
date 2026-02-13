from configparser import ConfigParser

class Config:
    def __init__(self, config_file="src/langgraph_agents/ui/ui_configfile.ini"):
        self.config = ConfigParser()
        self.config.read(config_file)

    def get_llm_options(self):
        return self.config["DEFAULT"].get("LLM_OPTIONS").split(", ")

    def usecase_options(self):
        return self.config["DEFAULT"].get("USECASE_OPTIONS").split(", ")

    def get_groq_models(self):
        return self.config["DEFAULT"].get("GROQ_MODEL_OPTIONS").split(", ")
    
    def page_title(self):
        return self.config["DEFAULT"].get("PAGE_TITLE")