from googleapiclient.errors import HttpError
from backend.utils import get_doc_service, get_drive_service

def test_doc():
  """
  Reference: https://developers.google.com/workspace/docs/api/quickstart/python

  Shows basic usage of the Docs API.
  Prints the title of a sample document.
  """
  DOCUMENT_ID = "195j9eDD3ccgjQRttHhJPymLJUCOUjs-jmwTrekvdjFE"

  try:
    document = get_doc_service().documents().get(documentId=DOCUMENT_ID).execute()

    assert document.get('title') is not None
    print(f"The title of the document is: {document.get('title')}")
  except HttpError as err:
    raise err
  except Exception as err:
    raise Exception(f"Unexpected error: {err}")

def test_drive():
  """
  Reference: https://developers.google.com/workspace/drive/api/quickstart/python

  Shows basic usage of the Drive API.
  Lists the names and ids of the first 10 files the user has access to.
  """
  try:
    results = (
        get_drive_service().files()
        .list(pageSize=10, fields="nextPageToken, files(id, name)")
        .execute()
    )
    items = results.get("files", [])

    if not items:
      print("No files found.")
    else:
      print("Files:")
      for item in items:
        print(f"{item['name']} ({item['id']})")

    assert isinstance(items, list)
  except HttpError as err:
    raise err
  except Exception as err:
    raise Exception(f"Unexpected error: {err}")
