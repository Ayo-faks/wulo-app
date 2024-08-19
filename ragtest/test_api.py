import requests
import json

# The base URL of your API
BASE_URL = "http://localhost:8000"

def test_root_endpoint():
    response = requests.get(f"{BASE_URL}/")
    print("Testing root endpoint (/)")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")
    print()

def test_search_endpoint(question):
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "question": question
    }
    response = requests.post(f"{BASE_URL}/search", headers=headers, data=json.dumps(data))
    print(f"Testing search endpoint (/search) with question: '{question}'")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")
    print()

if __name__ == "__main__":
    # Test the root endpoint
    test_root_endpoint()

    # Test the search endpoint with a few different questions
    test_questions = [
        "How does Charles Dickens portray Ebenezer Scrooge at the beginning of the story?",
        "What are the main themes in A Christmas Carol?",
        "Describe the character of Bob Cratchit.",
        "What is the significance of the three ghosts in the story?"
    ]

    for question in test_questions:
        test_search_endpoint(question)