import requests
import json

# Define the Groq API endpoint and API key
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
API_KEY = "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"  # Replace with your actual API key

def ask_groq(prompt):
    """
    Sends a prompt to the Groq API and prints the result.

    :param prompt: The text prompt to send to the Groq API.
    """
    # Define the headers for the API request
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    # Define the payload (request body)
    payload = {
        "model": "llama3-8b-8192",  # Model specified in the documentation
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }

    try:
        # Send the request to the API
        response = requests.post(GROQ_API_URL, headers=headers, json=payload)

        # Check if the request was successful
        if response.status_code == 200:
            result = response.json()
            # Extract and print the response content
            print("Response:")
            print(result["choices"][0]["message"]["content"])
        else:
            print(f"Error: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    user_prompt = input("Enter your prompt: ")
    ask_groq(user_prompt)