import requests
import json

# Define your Groq API endpoint and key
GROQ_API_URL = "https://api.groq.com/v1/completions"  # Replace with the actual endpoint
API_KEY = "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"  # Replace with your API key

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
        "model": "text-davinci-003",  # Replace with the model supported by Groq
        "prompt": prompt,
        "max_tokens": 150  # Adjust based on your needs
    }

    try:
        # Send the request to the API
        response = requests.post(GROQ_API_URL, headers=headers, data=json.dumps(payload))

        # Check if the request was successful
        if response.status_code == 200:
            result = response.json()
            # Extract and print the response text
            print("Response:")
            print(result.get("choices")[0].get("text"))
        else:
            print(f"Error: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    user_prompt = input("Enter your prompt: ")
    ask_groq(user_prompt)