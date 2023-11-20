# Import the 'requests' module for making HTTP requests.
import requests

# A simple in-memory database represented as a dictionary.
database = {
    1: "Alice",
    2: "Bob",
    3: "Charlie"
}

# Function to get a user from the in-memory database by user ID.


def get_user_from_db(user_id):
    return database.get(user_id)


# Function to retrieve a list of users from a remote API.


def get_users():
    # Make an HTTP GET request to a sample JSONPlaceholder API.
    response = requests.get("http://jsonplaceholder.typicode.com/users")


    # Check if the request was successful (status code 200).
    if response.status_code == 200:
        # Parse and return the JSON content of the response.
        return response.json()


    # Raise an HTTPError if the request was not successful.
    raise requests.HTTPError
