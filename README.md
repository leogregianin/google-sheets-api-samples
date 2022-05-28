# Read and Write Google Sheets API


## Prerequisites

* Create a Google Cloud Platform project with the API enabled. To create a project and enable an API, refer to https://developers.google.com/workspace/guides/create-project

* Create Authorization credentials with OAuth client ID in https://developers.google.com/workspace/guides/create-credentials#oauth-client-id


## Install the Google client library

* `pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib`


## Configure Google Sheets API credentials

Rename `credentials_sample.json` to `credentials.json` and fill in the following fields `client_id`, `project_id` and `client_secret`, or

Download json credentials file directly from `Google Cloud Platform > API Services > Credentials > OAuth client ID`.


## Run the samples

Change `SPREADSHEET_ID` to the ID of the Google Sheets spreadsheet you want to use.

* `python sheets_read.py` to read sheet data
* `python sheets_write.py` to write sheet data
