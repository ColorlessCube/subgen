import os

import requests

bark_url = os.environ.get('BARK_SERVER', 'https://api.day.app')
bark_token = os.environ.get('BARK_TOKEN', 'token')

if bark_url.endswith('/'):
    bark_url = bark_url[:-1]


def send_get_request(api_url, params):
    """
    Sends a GET request to the specified Bark API URL with the given parameters.

    Args:
        api_url (str): The URL of the Bark API.
        params (dict): The parameters to be sent with the GET request.

    Returns:
        Response: The response object from the GET request.
    """
    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # Return the response as JSON
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None


def bark_notify(message, params=None):
    """
    Sends a notification to Bark using the Bark API.

    Args:
        message (str): The message to be sent to Bark.
        params (dict): The parameters to be sent with the GET request.

    Returns:
        None
    """

    api_url = f'{bark_url}/{bark_token}/{message}'
    response = send_get_request(api_url, params)
    if response:
        print("Notification sent successfully!")
    else:
        print("Notification failed.")
