from langchain.tools import tool


@tool
def get_user_location_tool() -> str:
    """
    Get the location of the current user, city, state or country
    Returns:
      string represting user location
    """
    return "Ranchi, Jharkhand, India"
