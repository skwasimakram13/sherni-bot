from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

# Define the required scopes for YouTube Data API
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']

def authenticate():
    """Authenticate and return YouTube API client."""

    # Check if token.json already exists (for re-use)
    try:
        credentials = Credentials.from_authorized_user_file('token.json', SCOPES)
    except Exception as e:
        # If no valid credentials are found, run OAuth2 flow
        flow = InstalledAppFlow.from_client_secrets_file('youtube_credentials.json', SCOPES)
        credentials = flow.run_local_server(port=0)

        # Save credentials to token.json for later use
        with open('token.json', 'w') as token:
            token.write(credentials.to_json())

    # Build the YouTube API client
    youtube = build('youtube', 'v3', credentials=credentials)

    return youtube
