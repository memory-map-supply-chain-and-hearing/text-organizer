import os.path
import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

def test_quickstart():
  """
  Reference: https://developers.google.com/workspace/docs/api/quickstart/python
  
  Shows basic usage of the Docs API.
  Prints the title of a sample document.
  """
  SCOPES = ["https://www.googleapis.com/auth/documents.readonly"]
  DOCUMENT_ID = "195j9eDD3ccgjQRttHhJPymLJUCOUjs-jmwTrekvdjFE"

  try:
    creds, project = google.auth.default(scopes=SCOPES)
    service = build("docs", "v1", credentials=creds)

    # Retrieve the documents contents from the Docs service.
    document = service.documents().get(documentId=DOCUMENT_ID).execute()

    assert document.get('title') is not None
    print(f"The title of the document is: {document.get('title')}")
  except HttpError as err:
    raise err
  except Exception as err:
    raise Exception(f"Unexpected error: {err}")
