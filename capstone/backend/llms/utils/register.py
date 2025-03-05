from typing import Callable


def register_tool(method: Callable):
    """Decorator to register tool methods in the class"""
    method._is_tool = True  # Mark the method as a tool
    return method