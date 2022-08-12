import os.path
from typing import Any

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from sheets.helper import try_error


from sheets.abstractclasses import AbstractSheet


class CredentialsGoogle():

    SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets.readonly', 
    ]

    def __init__(self):

        self.__creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.json'):
             self.__creds = Credentials.from_authorized_user_file('token.json', self.SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not  self.__creds or not  self.__creds.valid:
            if  self.__creds and  self.__creds.expired and  self.__creds.refresh_token:
                 self.__creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', self.SCOPES)
                self.__creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.json', 'w') as token:
                token.write( self.__creds.to_json())

    def get_credentials(self):
        return self.__creds
        
    def __call__(self, *args, **kwds) -> Any:
        return self.get_credentials()


class Sheet(AbstractSheet):

    def __init__(self):
        self.cred = CredentialsGoogle()
        self.cred = self.cred.get_credentials()

    def build_service(self):
        try:
            service = build('sheets', 'v4', credentials=self.cred)
        except HttpError as e:
            print(e)
        return service
    
    @try_error
    def read_values(self, table, range=None):
        service = self.build_service()
        sheet = service.spreadsheets()
        result = sheet.values().get(
            spreadsheetId=table, 
            range=range
            ).execute()
        values = result.get('values', [])
        
        self.show(values)

    def get(self, spreadsheetId):
        service = self.build_service()
        sheets = service.spreadsheets()
        result = sheets.get(
            spreadsheetId,
            includeGridData=True
        )
        print(result)

    @try_error
    def read_patch_get(self, table, range=None):
        service = self.build_service()
        sheet = service.spreadsheets()
        result = sheet.values().batchGet(
            spreadsheetId=table, ranges=range
        ).execute()
        print(result)

        data = result.get("valueRanges", [])

    def write(self):
        print("work")

    def show(self, data):
        for i in data:
            print(*i)

    def read(self):
        pass

