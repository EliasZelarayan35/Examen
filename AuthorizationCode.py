import requests

def get_access_token_authorization_code(client_id, client_secret, redirect_uri, code, token_url):
    # Authentication parameters
    auth = (client_id, client_secret)

    # Parameters for token request
    data = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': redirect_uri
    }

    # Make the request to obtain the access token
    response = requests.post(token_url, auth=auth, data=data)
    response.raise_for_status()

    # Extract the access token from the response body
    access_token = response.json().get('access_token')

    return access_token

def test_api_with_authorization_code():
    client_id = 'your_client_id'
    client_secret = 'your_client_secret'
    redirect_uri = 'your_redirect_uri'
    authorization_code = 'authorization_code'
    token_url = 'token_endpoint_url'

    # Get the access token
    access_token = get_access_token_authorization_code(client_id, client_secret, redirect_uri, authorization_code, token_url)

    # Use the access token to make the API request
    api_url = "https://jsonplaceholder.typicode.com/albums"
    headers = {'Authorization': f'Bearer {access_token}'}

    try:
        # Make the API request with the access token
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()

        # Remaining code to verify and process the response...

        print("Successful test with 'Authorization Code' flow.")

    except requests.exceptions.RequestException as e:
        print(f"Error making API request: {e}")

if __name__ == "__main__":
    test_api_with_authorization_code()
