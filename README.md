# Read and Write Google Sheets API


## Prerequisites

* Create a Google Cloud Platform project with the API enabled. To create a project and enable an API, refer to https://developers.google.com/workspace/guides/create-project

* Create Authorization credentials with OAuth client ID (https://developers.google.com/workspace/guides/create-credentials#oauth-client-id)


## Install the Google client library

* `pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib`


## Configure the Google Sheets ID

Change `SPREADSHEET_ID` variable to the ID of the Google Sheets spreadsheet you want to use.


## Run the samples

* `python sheets_read.py` to read sheet data
* `python sheets_write.py` to write sheet data


Authorize the Google Sheets API
IDs do cliente OAuth 2.0


