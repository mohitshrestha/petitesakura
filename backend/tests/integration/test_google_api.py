import sys
import os

# Add the 'backend' directory to the sys.path so it can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

import json
from backend.app.api_clients.google_api import GoogleAPIClient
# from pprint import pprint  # To pretty-print complex objects
from rich import print # To pretty-print complex objects

def format_drive_files(files):
    """Format the list of Google Drive files for better readability."""
    if not files:
        return "No files found."
    formatted_files = "\n".join([f"- {file['name']} (ID: {file['id']})" for file in files])
    return formatted_files

def test_google_api_client():
    """Test the Google API client with both OAuth and Service Account."""
    print("Testing OAuth Authentication...")
    
    # OAuth Authentication
    google_client_oauth = GoogleAPIClient("drive", use_service_account=False)
    print("\n--- OAuth Authentication - Google Drive Files ---")
    drive_files_oauth = google_client_oauth.list_drive_files()
    print(format_drive_files(drive_files_oauth))  # Format the Drive files nicely

    # Service Account Authentication
    google_client_service_account = GoogleAPIClient("drive", use_service_account=True)
    print("\n--- Service Account Authentication - Google Drive Files ---")
    drive_files_service_account = google_client_service_account.list_drive_files()
    print(format_drive_files(drive_files_service_account))  # Format the Drive files nicely

if __name__ == "__main__":
    test_google_api_client()
