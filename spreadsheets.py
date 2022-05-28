import os
from time import sleep

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]


class Spreadsheet:
    def __init__(self, sheet_id):
        self.sheet_id = sheet_id
        self.failed = {
            "valueError": [],
            "error": []
        }

        creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES
                )
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.json', 'w') as token:
                token.write(creds.to_json())

        try:
            service = build("sheets", "v4", credentials=creds)

            # Call the Sheets API
            self.sheet = service.spreadsheets()
        except HttpError as err:
            print(f"HttpError {err}")

    def getSpreadsheet(self):
        return self.sheet


class MySheets:
    def __init__(self, spreadsheet_id):
        self.spreadsheet_id = spreadsheet_id

        sheet = Spreadsheet(spreadsheet_id)
        self.spreadsheet = sheet.getSpreadsheet()

    def read_data_sheet(self, data_range):
        try:
            raw_data = (
                self.spreadsheet.values()
                .get(
                    spreadsheetId=self.spreadsheet_id,
                    range=data_range,
                    majorDimension="COLUMNS",
                )
                .execute()
                .get("values", [])
            )

            return raw_data
        except Exception as err:
            return(f'read_data_sheet() error: {err}')

    def write_data_sheet(self, data_range, data_update: list):
        try:
            body = {
                "range": data_range,
                "majorDimension": "ROWS",
                "values": data_update
            }

            raw_data = (
                self.spreadsheet.values()
                .update(
                    spreadsheetId=self.spreadsheet_id,
                    range=data_range,
                    valueInputOption="USER_ENTERED",
                    body=body
                )
                .execute()
            )
            return raw_data

        except Exception as err:
            return(f'read_data_sheet() error: {err}')
