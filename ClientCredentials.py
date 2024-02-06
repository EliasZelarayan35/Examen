import requests

def get_access_token_client_credentials(client_id, client_secret, token_url):
    # Authentication parameters
    auth = (client_id, client_secret)

    # Parameters for token request
    data = {
        'grant_type': 'client_credentials'
    }

    # Make the request to obtain the access token
    response = requests.post(token_url, auth=auth, data=data)
    response.raise_for_status()

    # Extract the access token from the response body
    access_token = response.json().get('access_token')

    return access_token

def test_api_with_client_credentials():
    client_id = 'your_client_id'
    client_secret = 'your_client_secret'
    token_url = 'token_endpoint_url'

    # Get the access token
    access_token = get_access_token_client_credentials(client_id, client_secret, token_url)

    # Use the access token to make the API request
    api_url = "https://jsonplaceholder.typicode.com/albums"
    headers = {'Authorization': f'Bearer {access_token}'}

    try:
        # Make the API request with the access token
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()

        # Remaining code to verify and process the response...

        print("Successful test with 'Client Credentials' flow.")

    except requests.exceptions.RequestException as e:
        print(f"Error making API request: {e}")

if __name__ == "__main__":
    test_api_with_client_credentials()
