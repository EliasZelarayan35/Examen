import requests

def validate_api_response(api_url, expected_texts):
    try:
        # Make the API request
        response = requests.get(api_url)
        response.raise_for_status()

        # Get the first five elements from the API response
        albums = response.json()[:5]

        # Validate if the text matches the expected results
        for album, expected_text in zip(albums, expected_texts):
            assert album["title"] == expected_text, f"Error: Expected text: '{expected_text}', Actual text: '{album['title']}'"

        print("API response validation successful: Texts match the expected values.")

    except requests.exceptions.RequestException as e:
        print(f"Error making API request: {e}")

# URL for the API call
api_url = "https://jsonplaceholder.typicode.com/albums"

# Expected texts for validation
expected_text = ""

# Validate the API response
validate_api_response(api_url, expected_text)
