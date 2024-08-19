# import json
# import requests
# from langchain.tools import tool

# class ChatTools:

#     @tool("Send chat message")
#     def send_chat_message(message: str) -> str:
#         """Useful to search neo4 databse of searching a Neo4j database for legal questions, analytics-related queries, and assisting in document writing processes about a given topic and return relevant
#     results.."""
#         url = 'http://127.0.0.1:8000/api/chat'
#         payload = {'message': message}
#         try:
#             response = requests.post(url, json=payload)
#             response.raise_for_status()  # Raise an error for bad status codes
#             data = response.json()
#             print("Raw response data:", data)  # Debug: Print raw response data
#             return f"Response from API: {data.get('response', 'No response found in response.')}"
#         except requests.exceptions.RequestException as e:
#             return f"An error occurred: {e}"

# # # Example usage
# # if __name__ == "__main__":
# #     chat_tool = ChatTools()
# #     result = chat_tool.send_chat_message("What is the primary business of Svenska Petroleum Exploration AB?")
# #     print(result)
import requests
import json
from langchain.tools import tool
# The base URL of your API (configurable)
BASE_URL = "http://localhost:8000"  # You can change this URL

class SearchTool:

  @tool("Search using your API")
  def search(self, question: str) -> str:
    """
    Sends a search query to your API and returns the response.

    Args:
        question: The question to be searched.

    Returns:
        A string containing the response from the API, or an error message.
    """
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "question": question
    }
    url = f"{BASE_URL}/search"  # Assuming your search endpoint is "/search"

    try:
      response = requests.post(url, headers=headers, data=json.dumps(data))
      response.raise_for_status()
      return response.json().get('response', 'No response found.')
    except requests.exceptions.RequestException as e:
      return f"An error occurred: {e}"

# # Example usage (optional)
# if __name__ == "__main__":
#   search_tool = SearchTool()
#   question = "What is the capital of France?"
#   result = search_tool.search(question)
#   print(result)