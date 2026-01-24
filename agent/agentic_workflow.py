from utils.model_loader import ModelLoader
from prompt_library.prompt import SYSTEM_PROMPT
from langgraph.graph import StateGraph, MessagesState, END, START
from langgraph.prebuilt import ToolNode, tools_condition

from tools.weather_info_tool import WeatherInfoTool
from tools.place_search_tool import PlaceSearchTool
from tools.expense_calculator_tool import CalculatorTool
from tools.currency_conversion_tool import CurrencyConverterTool

class GraphBuilder():
    def __init__(self):
        pass
    
    
    def agent_function(self):
        pass
    
    def build_graph(self):
        pass
    
    
    # __call__ is a special method in Python that allows an object to be called like a function.
    # When you define __call__ inside a class, instances of that class become callable.
    def __call__(self):
        pass
    