import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from dotenv import load_dotenv
import logging

# Load environment variables from .env
load_dotenv()

# Fetch credentials file paths securely from environment variables
client_secret_path = os.getenv("GOOGLE_CLIENT_SECRET_PATH")
service_account_path = os.getenv("GOOGLE_SERVICE_ACCOUNT_PATH")
token_file_path = os.getenv("GOOGLE_TOKEN_PATH", "token.json")  # Default token file path, can be overridden by env variable

# Create directory if it doesn't exist
token_dir = os.path.dirname(token_file_path)
if not os.path.exists(token_dir):
    os.makedirs(token_dir)
    
# Define SCOPES for Google APIs you need access to
SCOPES = {
    "drive": [
        "https://www.googleapis.com/auth/drive",  # for full access to Google Drive
        "https://www.googleapis.com/auth/drive.file",  # for file-specific access
        "https://www.googleapis.com/auth/drive.readonly",  # for readonly access
    ],
    "sheets": ["https://www.googleapis.com/auth/spreadsheets"],  # for Google Sheets
    "gmail": ["https://www.googleapis.com/auth/gmail.readonly"],  # for Gmail
    "calendar": ["https://www.googleapis.com/auth/calendar"],  # for Google Calendar
    "docs": ["https://www.googleapis.com/auth/documents.readonly"],  # for Google Docs
    "slides": ["https://www.googleapis.com/auth/presentations.readonly"],  # for Google Slides
}

API_VERSIONS = {
    "drive": "v3",  # Google Drive uses v3
    "sheets": "v4",  # Google Sheets uses v4
    "gmail": "v1",  # Gmail uses v1
    "calendar": "v3",  # Google Calendar uses v3
    "docs": "v1",  # Google Docs uses v1
    "slides": "v1",  # Google Slides uses v1
}

class GoogleAPIClient:
    def __init__(self, api_name: str, use_service_account=False):
        """Initialize the Google API client for a specific service."""
        self.api_name = api_name
        self.credentials = None
        self.service = None
        self.use_service_account = use_service_account
        self._authenticate()

    def _authenticate(self):
        """Authenticate and create the API client."""
        creds = None
        # Choose authentication method based on user input or environment settings
        if self.use_service_account:
            creds = self._authenticate_with_service_account()
        else:
            creds = self._authenticate_with_oauth()

        # Build the appropriate Google API service client
        self.service = build(self.api_name, API_VERSIONS[self.api_name], credentials=creds)

    def _authenticate_with_oauth(self):
        """Authenticate using OAuth (User Login)."""
        creds = None
        # Check if token exists
        if os.path.exists(token_file_path):
            creds = Credentials.from_authorized_user_file(token_file_path, SCOPES[self.api_name])

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                # OAuth flow to generate a new token if needed
                flow = InstalledAppFlow.from_client_secrets_file(
                    client_secret_path, SCOPES[self.api_name]
                )
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run securely
            with open(token_file_path, 'w') as token:
                token.write(creds.to_json())
        return creds

    def _authenticate_with_service_account(self):
        """Authenticate using Service Account."""
        from google.oauth2 import service_account
        creds = service_account.Credentials.from_service_account_file(
            service_account_path,
            scopes=SCOPES[self.api_name]
        )
        return creds

    def get_service(self):
        """Return the authenticated API service."""
        if self.service is None:
            raise ValueError(f"{self.api_name} client is not authenticated.")
        return self.service

    # Google Drive API: List files (including shared drives)
    def list_drive_files(self):
        """List files from Google Drive, including shared drives."""
        drive_service = self.get_service()
        results = drive_service.files().list(
            pageSize=10,
            fields="files(id, name)",
            corpora="allDrives",  # Include shared drives
            includeItemsFromAllDrives=True,
            supportsAllDrives=True
        ).execute()
        return results.get('files', [])

    # Google Sheets API: Read a range from a spreadsheet
    def read_spreadsheet(self, spreadsheet_id: str, range_name: str):
        """Read a range from a Google Sheets spreadsheet."""
        sheets_service = self.get_service()
        result = sheets_service.spreadsheets().values().get(
            spreadsheetId=spreadsheet_id, range=range_name
        ).execute()
        return result.get('values', [])

    # Google Docs API: Read a document
    def read_document(self, document_id: str):
        """Read a Google Docs document."""
        docs_service = self.get_service()
        document = docs_service.documents().get(documentId=document_id).execute()
        return document

    # Google Gmail API: List emails
    def list_emails(self):
        """List emails from Gmail."""
        gmail_service = self.get_service()
        results = gmail_service.users().messages().list(userId='me').execute()
        return results.get('messages', [])

    # Google Calendar API: List events
    def list_calendar_events(self):
        """List upcoming events from Google Calendar."""
        calendar_service = self.get_service()
        events_result = calendar_service.events().list(
            calendarId='primary', timeMin='2023-01-01T00:00:00Z'
        ).execute()
        return events_result.get('items', [])

    # Google Slides API: Read presentations
    def read_presentation(self, presentation_id: str):
        """Read a Google Slides presentation."""
        slides_service = self.get_service()
        presentation = slides_service.presentations().get(
            presentationId=presentation_id
        ).execute()
        return presentation
