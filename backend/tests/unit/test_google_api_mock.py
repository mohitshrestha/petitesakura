# backend/tests/unit/test_google_api_mock.py
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

import pytest
from unittest import mock
from backend.app.api_clients.google_api import GoogleAPIClient

@mock.patch.object(GoogleAPIClient, 'list_drive_files', return_value=[{"name": "testfile", "id": "123"}])
def test_google_api_client_with_mock(mock_list_drive_files):
    """Test the Google API client with mocked responses."""
    google_client_oauth = GoogleAPIClient("drive", use_service_account=False)
    drive_files_oauth = google_client_oauth.list_drive_files()
    assert len(drive_files_oauth) == 1
    assert drive_files_oauth[0]['name'] == "testfile"
