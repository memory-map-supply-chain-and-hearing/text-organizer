import google.auth
from googleapiclient.discovery import build

def get_doc_service():
    """
    Returns a Google Docs v1 service using Application Default Credentials.
    """
    SCOPES = ["https://www.googleapis.com/auth/documents.readonly"]
    creds, project = google.auth.default(scopes=SCOPES)
    return build("docs", "v1", credentials=creds)

def get_drive_service():
    """
    Returns a Google Drive v3 service using Application Default Credentials.
    """
    SCOPES = ["https://www.googleapis.com/auth/drive.metadata.readonly"]
    creds, project = google.auth.default(scopes=SCOPES)
    return build("drive", "v3", credentials=creds)
