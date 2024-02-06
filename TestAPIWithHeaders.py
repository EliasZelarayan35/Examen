import requests
from requests.auth import HTTPBasicAuth

def authenticate_client_credentials():
    # Authentication parameters
    client_id = 'your_client_id'
    client_secret = 'your_client_secret'
    token_url = 'https://your_auth_server.com/token'

    # Requesting access token using Client Credentials grant type
    response = requests.post(token_url, auth=HTTPBasicAuth(client_id, client_secret), data={'grant_type': 'client_credentials'})

    # Extracting access token from response
    if response.status_code == 200:
        access_token = response.json()['access_token']
        return access_token
    else:
        raise Exception(f"Failed to authenticate using Client Credentials: {response.text}")

def authenticate_authorization_code():
    # Authentication parameters
    client_id = 'your_client_id'
    client_secret = 'your_client_secret'
    authorization_url = 'https://your_auth_server.com/authorize'
    token_url = 'https://your_auth_server.com/token'
    redirect_uri = 'https://your_redirect_uri.com'
    authorization_code = 'your_authorization_code'

    # Obtaining authorization code (manually or via automated browser)
    # Redirect the user to the authorization URL and obtain the authorization code

    # Exchange authorization code for access token
    response = requests.post(token_url, data={'grant_type': 'authorization_code', 'client_id': client_id, 'client_secret': client_secret, 'code': authorization_code, 'redirect_uri': redirect_uri})

    # Extracting access token from response
    if response.status_code == 200:
        access_token = response.json()['access_token']
        return access_token
    else:
        raise Exception(f"Failed to authenticate using Authorization Code: {response.text}")

def test_api(access_token, expected_text):
    try:
        # API endpoint URL
        url = "https://jsonplaceholder.typicode.com/albums"

        # Send GET request to the API with Authorization header containing access token
        headers = {'Authorization': f'Bearer {access_token}'}
        response = requests.get(url, headers=headers)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Extract data from the response
            data = response.json()

            # Validate the text of the first five elements
            for i in range(5):
                actual_text = data[i]["title"]
                if actual_text == expected_text:
                    print(f"Element {i+1}: Text matches expected.")
                else:
                    print(f"Element {i+1}: Text does not match expected.")

        else:
            print(f"Request failed with status code {response.status_code}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # Expected text for validation
    expected_text = "Test text"

    # Authenticate using Client Credentials grant type
    access_token_cc = authenticate_client_credentials()

    # Authenticate using Authorization Code grant type
    access_token_ac = authenticate_authorization_code()

    # Test the API with Client Credentials authentication
    print("Testing API with Client Credentials authentication:")
    test_api(access_token_cc, expected_text)

    # Test the API with Authorization Code authentication
    print("\nTesting API with Authorization Code authentication:")
    test_api(access_token_ac, expected_text)
