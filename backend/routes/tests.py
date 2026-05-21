
import os.path
from fastapi import APIRouter
#from google.auth.transport.requests import Request
#from google.oauth2.credentials import Credentials
#from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

router = APIRouter()

@router.get("/quickstart")
def quickstart():
  """
  Reference: https://developers.google.com/workspace/docs/api/quickstart/python

  Shows basic usage of the Docs API.
  Prints the title of a sample document.
  """
  SCOPES = ["https://www.googleapis.com/auth/documents.readonly"]
  DOCUMENT_ID = "195j9eDD3ccgjQRttHhJPymLJUCOUjs-jmwTrekvdjFE"

  creds = None
  # The file token.json stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.
  if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          "credentials.json", SCOPES
      )
      creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open("token.json", "w") as token:
      token.write(creds.to_json())

  try:
    service = build("docs", "v1", credentials=creds)

    # Retrieve the documents contents from the Docs service.
    document = service.documents().get(documentId=DOCUMENT_ID).execute()

    return f"The title of the document is: {document.get('title')}"
  except HttpError as err:
    return err
