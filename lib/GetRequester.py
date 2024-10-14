import requests
import json

class GetRequester:
    
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        # Send a GET request and return the response as bytes
        response = requests.get(self.url)
        return response.content  # Return the response as bytes

    def load_json(self):
        # Parse the response body as JSON and return a Python object
        response_body = self.get_response_body().decode('utf-8')  # Decode bytes to string
        return json.loads(response_body)  # Convert the JSON string to a Python object
