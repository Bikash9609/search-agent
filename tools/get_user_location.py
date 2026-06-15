from langchain.tools import tool


@tool
def get_user_location_tool() -> str:
    """
    Get current the location of the current user
    Returns:
      string represting user location
    """
    return "Ranchi, Jharkhand, India"
